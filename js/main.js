(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  // mobile menu
  var b=$('#burger'),n=$('#nav');
  if(b)b.onclick=function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)};
  $$('#nav a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('open')})});
  // hide header on scroll down
  var h=$('#hdr'),last=0;
  addEventListener('scroll',function(){var y=scrollY;h.classList.toggle('hide',y>last&&y>200);last=y},{passive:true});
  // hero slideshow
  var sl=$$('.slide'),dots=$$('#dots button'),i=0,t;
  function go(k){sl[i].classList.remove('on');dots[i]&&dots[i].classList.remove('on');i=(k+sl.length)%sl.length;sl[i].classList.add('on');dots[i]&&dots[i].classList.add('on')}
  if(sl.length>1){t=setInterval(function(){go(i+1)},5000);dots.forEach(function(d,k){d.onclick=function(){clearInterval(t);go(k)}})}
  // scroll reveal
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
    $$('.scol,.pcard,.vals>div,.welcome .wrap').forEach(function(el){el.classList.add('rv');io.observe(el)});
  }
  // lightbox
  var lb=$('#lb');
  if(lb){
    var items=$$('.gi'),li=0,im=$('img',lb);
    function show(k){li=(k+items.length)%items.length;im.src=items[li].getAttribute('href')}
    items.forEach(function(a,k){a.onclick=function(e){e.preventDefault();show(k);lb.hidden=false}});
    $('.lb-x').onclick=function(){lb.hidden=true};
    $('.lb-p').onclick=function(){show(li-1)};$('.lb-n').onclick=function(){show(li+1)};
    lb.onclick=function(e){if(e.target===lb)lb.hidden=true};
    addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')lb.hidden=true;if(e.key==='ArrowLeft')show(li-1);if(e.key==='ArrowRight')show(li+1)});
  }
  // contact form -> opens visitor's mail app (works on any static host)
  var f=$('#cform');
  if(f)f.onsubmit=function(e){
    e.preventDefault();var d=new FormData(f),note=$('#cnote');
    if(!d.get('name')||!d.get('email')||!d.get('msg')){note.textContent='Please fill in name, email and message.';return}
    var body='Name: '+d.get('name')+'\nPhone: '+d.get('phone')+'\nEmail: '+d.get('email')+'\n\n'+d.get('msg');
    location.href='mailto:'+window.CONTACT_EMAIL+'?subject='+encodeURIComponent('Website enquiry from '+d.get('name'))+'&body='+encodeURIComponent(body);
    note.textContent='Opening your email app… if nothing opens, email us directly at '+window.CONTACT_EMAIL+'.';
  };
})();
