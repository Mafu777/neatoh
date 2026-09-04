document.getElementById('navToggle').addEventListener('click', function(){
  document.getElementById('navLinks').classList.toggle('open');
});

var quoteForm = document.getElementById('quoteForm');

if (quoteForm) {
  quoteForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var form = e.target;
    var data = new FormData(form);

    fetch(form.action, {
      method: 'POST',
      body: data,
      headers: { 'Accept': 'application/json' }
    }).then(function(response) {
      if (response.ok) {
        document.getElementById('form-success').style.display = 'block';
        form.reset();
      } else {
        alert('Sorry, something went wrong. Please try again or email us directly.');
      }
    }).catch(function() {
      alert('Sorry, something went wrong. Please try again or email us directly.');
    });
  });
}
var header = document.getElementById('siteHeader');
window.addEventListener('scroll', function(){
  header.classList.toggle('scrolled', window.scrollY > 40);
});

var revealTargets = document.querySelectorAll('[data-reveal], [data-reveal-stagger]');
var processGrid = document.getElementById('processGrid');

if('IntersectionObserver' in window){
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('in-view');
        io.unobserve(entry.target);
      }
    });
  }, {threshold:0.15});
  revealTargets.forEach(function(el){ io.observe(el); });

  if(processGrid){
    var lineIo = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('in-view');
          lineIo.unobserve(entry.target);
        }
      });
    }, {threshold:0.3});
    lineIo.observe(processGrid);
  }
} else {
  revealTargets.forEach(function(el){ el.classList.add('in-view'); });
  if(processGrid){ processGrid.classList.add('in-view'); }
}
