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
  // contact form -> FormSubmit (free) sends the message to the business inbox; mailto is a fallback
  var f=$('#cform');
  if(f)f.onsubmit=function(e){
    e.preventDefault();
    var d=new FormData(f),note=$('#cnote'),btn=$('button[type=submit]',f);
    if(d.get('_honey'))return;
    if(!d.get('name')||!d.get('email')||!d.get('msg')){note.textContent='Please fill in name, email and message.';return}
    btn.disabled=true;note.textContent='Sending…';
    var data={name:d.get('name'),phone:d.get('phone')||'-',email:d.get('email'),message:d.get('msg'),_subject:'New website enquiry from '+d.get('name'),_template:'table',_replyto:d.get('email')};
    fetch('https://formsubmit.co/ajax/'+window.CONTACT_EMAIL,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json()}).then(function(j){
        if(j.success==='true'||j.success===true){f.reset();note.textContent='Thank you! Your message has been sent. We will get back to you shortly.'}
        else throw new Error('fail')
      }).catch(function(){
        note.innerHTML='Sorry, we could not send your message. Please call '+window.CONTACT_PHONE+' or <a href="mailto:'+window.CONTACT_EMAIL+'">email us</a>.'
      }).then(function(){btn.disabled=false});
  };
})();
