/** Coordinate the first-paint HTML intro while the application loads in parallel. */
import {useEffect} from 'react';

/** Ring once on a fresh page load; normal in-app navigation does not replay it. */
export function useStartupIntro(){
  useEffect(()=>{
    const splash=document.getElementById('startup-splash');
    if(!splash)return;
    const animation=splash.querySelector('.startup-bell')?.getAnimations()[0];
    const elapsed=typeof animation?.currentTime==='number'?animation.currentTime:0;
    let finish:ReturnType<typeof setTimeout>|undefined;
    const timer=setTimeout(()=>{
      splash.classList.add('is-leaving');
      finish=setTimeout(()=>{
        splash.remove();
        document.body.classList.remove('is-starting');
        const root=document.getElementById('root');
        root?.removeAttribute('inert');
        root?.removeAttribute('aria-hidden');
      },200);
    },Math.max(0,2800-elapsed));
    return()=>{clearTimeout(timer);if(finish)clearTimeout(finish);};
  },[]);
}
