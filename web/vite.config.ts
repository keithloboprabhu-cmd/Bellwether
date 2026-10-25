/** Development proxy; production is served with the Python snapshot API. */
import { defineConfig } from 'vite';
export default defineConfig({server: {proxy: {'/api': 'http://127.0.0.1:8787'}}});
