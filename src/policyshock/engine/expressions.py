"""Safe arithmetic expressions for policy configs (no eval of arbitrary code).

Policy YAML parameters can be numbers or expressions such as
    "input.tariff_pct / 100 * exposure.import_share_of_cogs"
    "input.oil_price_override if input.oil_price_override is not None else derived.base_move"
Names must be `<namespace>.<key>`; allowed namespaces are listed in NAMESPACES.
Only arithmetic, comparisons, conditionals and min/max/abs are permitted, so adding a
policy can never run arbitrary code.
"""

from __future__ import annotations

import ast
import operator
from functools import lru_cache
from typing import Any, Mapping

NAMESPACES = ("input", "assumption", "exposure", "baseline", "derived", "macro", "role")

_BIN = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}
_CMP = {
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Is: operator.is_,
    ast.IsNot: operator.is_not,
}
_FUNCS = {"min": min, "max": max, "abs": abs}


class ExpressionError(ValueError):
    pass


@lru_cache(maxsize=4096)
def parse(expr: str) -> ast.Expression:
    """Parse and safety-check an expression (cached: policies re-evaluate the same strings)."""
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError as exc:
        raise ExpressionError(f"cannot parse expression {expr!r}: {exc}") from exc
    _check(tree.body, expr)
    return tree


def _check(node: ast.AST, expr: str) -> None:
    """Reject any syntax outside the small allowed subset."""
    if isinstance(node, ast.Constant):
        if not isinstance(node.value, (int, float, str)) and node.value is not None:
            raise ExpressionError(f"constant {node.value!r} not allowed in {expr!r}")
    elif isinstance(node, ast.Attribute):
        if not (isinstance(node.value, ast.Name) and node.value.id in NAMESPACES):
            raise ExpressionError(f"names must look like namespace.key ({', '.join(NAMESPACES)}) in {expr!r}")
    elif isinstance(node, ast.BinOp) and type(node.op) in _BIN:
        _check(node.left, expr)
        _check(node.right, expr)
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        _check(node.operand, expr)
    elif isinstance(node, ast.IfExp):
        for n in (node.test, node.body, node.orelse):
            _check(n, expr)
    elif isinstance(node, ast.Compare) and all(type(o) in _CMP for o in node.ops):
        for n in (node.left, *node.comparators):
            _check(n, expr)
    elif isinstance(node, ast.BoolOp):
        for n in node.values:
            _check(n, expr)
    elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCS:
        for n in node.args:
            _check(n, expr)
    else:
        raise ExpressionError(f"unsupported syntax {type(node).__name__} in {expr!r}")


def references(expr: str | float | int) -> set[tuple[str, str]]:
    """All (namespace, key) pairs an expression refers to (empty for plain numbers)."""
    if not isinstance(expr, str):
        return set()
    tree = parse(expr)
    return {(n.value.id, n.attr) for n in ast.walk(tree) if isinstance(n, ast.Attribute)}


def evaluate(expr: str | float | int | None, context: Mapping[str, Mapping[str, Any]]) -> Any:
    """Evaluate an expression against {namespace: {key: value}}. Numbers pass through."""
    if expr is None or isinstance(expr, (int, float)):
        return expr
    tree = parse(expr)
    return _eval(tree.body, context, expr)


def _eval(node: ast.AST, ctx: Mapping[str, Mapping[str, Any]], expr: str) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Attribute):
        ns, key = node.value.id, node.attr
        try:
            return ctx[ns][key]
        except KeyError as exc:
            raise ExpressionError(f"unknown name {ns}.{key} in {expr!r}") from exc
    if isinstance(node, ast.BinOp):
        return _BIN[type(node.op)](_eval(node.left, ctx, expr), _eval(node.right, ctx, expr))
    if isinstance(node, ast.UnaryOp):
        v = _eval(node.operand, ctx, expr)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.IfExp):
        return _eval(node.body, ctx, expr) if _eval(node.test, ctx, expr) else _eval(node.orelse, ctx, expr)
    if isinstance(node, ast.Compare):
        left = _eval(node.left, ctx, expr)
        for op, comp in zip(node.ops, node.comparators):
            right = _eval(comp, ctx, expr)
            if not _CMP[type(op)](left, right):
                return False
            left = right
        return True
    if isinstance(node, ast.BoolOp):
        vals = [_eval(v, ctx, expr) for v in node.values]
        return all(vals) if isinstance(node.op, ast.And) else any(vals)
    if isinstance(node, ast.Call):
        return _FUNCS[node.func.id](*(_eval(a, ctx, expr) for a in node.args))
    raise ExpressionError(f"unsupported syntax in {expr!r}")  # unreachable after _check
