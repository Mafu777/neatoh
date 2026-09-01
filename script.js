document.getElementById('navToggle').addEventListener('click', function(){
  document.getElementById('navLinks').classList.toggle('open');
});

document.getElementById('quoteForm').addEventListener('submit', function(e){
  e.preventDefault();
  document.getElementById('form-success').style.display = 'block';
  this.reset();
});

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
