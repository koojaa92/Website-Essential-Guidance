(function(){
  var bar=document.getElementById('prog');
  function upd(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  window.addEventListener('scroll',upd,{passive:true});
  window.addEventListener('resize',upd);upd();
})();
(function(){
  var links=document.querySelectorAll('#mainnav a');
  if(!links.length) return;
  var ids=Array.prototype.map.call(links,function(a){return a.getAttribute('href').slice(1);});
  var targets=ids.map(function(id){return document.getElementById(id);}).filter(Boolean);
  function upd(){
    var current='';
    targets.forEach(function(sec){
      var r=sec.getBoundingClientRect();
      if(r.top<=140 && r.bottom>=140) current=sec.id;
    });
    links.forEach(function(a){
      a.classList.toggle('active', a.getAttribute('href')==='#'+current);
    });
  }
  window.addEventListener('scroll',upd,{passive:true});
  upd();
})();

// Termine automatisch filtern: vergangene Termine immer ausblenden;
// auf Containern mit data-max-count zusätzlich nur die naechsten N anstehenden zeigen
(function(){
  var containers = document.querySelectorAll('.dates');
  if(!containers.length) return;
  var today = new Date();
  today.setHours(0,0,0,0);

  containers.forEach(function(container){
    var maxCount = container.getAttribute('data-max-count');
    var category = container.getAttribute('data-category'); // z.B. "raum" -- nur Termine dieser Kategorie
    var cards = Array.prototype.slice.call(container.querySelectorAll('.dcard[data-date]'));

    // erst alles ausblenden, dann gezielt einblenden -- vermeidet Flackern falscher Reihenfolge
    cards.forEach(function(card){ card.style.display = 'none'; });

    if(category){
      cards = cards.filter(function(card){ return card.classList.contains(category); });
    }

    var upcoming = cards.filter(function(card){
      return new Date(card.getAttribute('data-date') + 'T00:00:00') >= today;
    }).sort(function(a,b){
      return new Date(a.getAttribute('data-date')) - new Date(b.getAttribute('data-date'));
    });

    var toShow = upcoming;
    if(maxCount){
      var lim = parseInt(maxCount,10);
      toShow = upcoming.slice(0, lim);
      // Sicherstellen, dass der naechste Essenz Raum-Termin sichtbar ist (nur relevant ohne Kategorie-Filter)
      if(!category){
        var hasRaum = toShow.some(function(c){ return c.classList.contains('raum'); });
        if(!hasRaum){
          var nextRaum = upcoming.find(function(c){ return c.classList.contains('raum'); });
          if(nextRaum){ toShow = toShow.slice(0, lim-1).concat([nextRaum]); }
        }
      }
    }
    toShow.forEach(function(card){ card.style.display = ''; });
    if(!toShow.length){
      var note = document.createElement('p');
      note.className = 'dates-empty';
      note.textContent = 'Aktuell sind keine Termine eingetragen. Neue Termine gibt es im Telegram-Kanal und im Newsletter.';
      container.appendChild(note);
      container.style.display = 'block';
    }
  });
})();

// Mobiles Menü: Hamburger öffnet/schließt die Navigation
(function(){
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('mainnav');
  if(!toggle || !nav) return;
  toggle.addEventListener('click', function(){
    nav.classList.toggle('open');
  });
  nav.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){ nav.classList.remove('open'); });
  });
})();

// Dynamisches "Nächster Termin"-Badge im Hero
(function(){
  var badge = document.getElementById('hero-badge-text');
  if(!badge) return;
  var cards = document.querySelectorAll('#dates-home .dcard[data-date]');
  if(!cards.length) return;
  var today = new Date(); today.setHours(0,0,0,0);
  var months = ['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'];
  var upcoming = Array.prototype.map.call(cards, function(card){
    return { date: new Date(card.getAttribute('data-date') + 'T00:00:00'), title: (card.querySelector('h3')||{}).textContent || '' };
  }).filter(function(e){ return e.date >= today; })
    .sort(function(a,b){ return a.date - b.date; });
  if(upcoming.length){
    var next = upcoming[0];
    var d = next.date;
    badge.innerHTML = 'Nächster Termin: <b>' + d.getDate() + '. ' + months[d.getMonth()] + ', ' + next.title + '</b>';
  } else {
    badge.parentElement.style.display = 'none';
  }
})();

// Formen der Begleitung: Karte anklicken -> goldener Balken + Detail klappt auf
(function(){
  var cards = document.querySelectorAll('.paket[data-panel]');
  if(!cards.length) return;
  var panels = document.querySelectorAll('.paket-panel');
  cards.forEach(function(card){
    card.setAttribute('aria-expanded','false');
    card.setAttribute('aria-controls', card.getAttribute('data-panel'));
    card.addEventListener('click', function(){
      var id = card.getAttribute('data-panel');
      var wasOpen = card.classList.contains('is-open');
      cards.forEach(function(c){ c.classList.remove('is-open'); c.setAttribute('aria-expanded','false'); });
      panels.forEach(function(p){ p.classList.remove('is-open'); });
      if(!wasOpen){
        card.classList.add('is-open');
        card.setAttribute('aria-expanded','true');
        var panel = document.getElementById(id);
        if(panel) panel.classList.add('is-open');
      }
    });
  });
})();

// Sanftes Einblenden beim Scrollen
(function(){
  if(!('IntersectionObserver' in window)) return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = Array.prototype.slice.call(
    document.querySelectorAll('section:not(.hero) > .wrap, img.imgband')
  );
  if(!els.length) return;
  els.forEach(function(el){ el.classList.add('reveal'); });
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){ e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -6% 0px', threshold: 0.04 });
  els.forEach(function(el){ io.observe(el); });
  // Sicherheitsnetz: nach spaetestens 1.5s alles zeigen, falls der Observer nicht (rechtzeitig) greift
  setTimeout(function(){ els.forEach(function(el){ el.classList.add('is-in'); }); }, 1500);
})();

// SoundCloud-Player erst nach Klick laden (Datenschutz)
(function(){
  var box = document.getElementById('sc-consent');
  if(!box) return;
  var btn = box.querySelector('button');
  btn.addEventListener('click', function(){
    var f = document.createElement('iframe');
    f.className = 'sc-solo';
    f.style.height = '20rem';
    f.setAttribute('scrolling','no');
    f.setAttribute('frameborder','no');
    f.setAttribute('allow','autoplay');
    f.setAttribute('title','J Kobi auf SoundCloud \u2014 aktuelle Sets');
    f.src = box.getAttribute('data-src');
    box.replaceWith(f);
  });
})();
