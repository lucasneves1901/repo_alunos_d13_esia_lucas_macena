(()=>{const slides=[...document.querySelectorAll('.slide')];let current=0;const counter=document.querySelector('.counter');
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',i===current?'false':'true')});counter.textContent=`${current+1} / ${slides.length}`;history.replaceState(null,'',`#slide-${current+1}`)}
// Avançar primeiro revela a resposta comentada do slide; o avanço seguinte troca de slide.
function next(){const pending=slides[current].querySelector('.resposta:not(.revelada)');if(pending){pending.classList.add('revelada');return}show(current+1)}
document.querySelector('#prev').addEventListener('click',()=>show(current-1));document.querySelector('#next').addEventListener('click',next);
document.addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();next()}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(current-1)}if(e.key==='Home')show(0);if(e.key==='End')show(slides.length-1);if(e.key.toLowerCase()==='f'){if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen().catch(()=>{})}});
const wanted=parseInt(location.hash.replace('#slide-',''),10);show(Number.isFinite(wanted)?wanted-1:0);window.d13Show=show;
})();
