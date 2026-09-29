/* Werkstatt: Texte direkt auf der Seite bearbeiten, Bilder per Klick ersetzen.
   Aenderungen liegen als kleine Ueberschreib-Liste in overrides.js; die Seiten selbst bleiben unveraendert. */
(function(){
  var STASH = 'eg-werkstatt';
  var served = window.W_OVERRIDES || {rev: 0, t: {}, i: {}};
  var ov = {rev: served.rev || 0, t: Object.assign({}, served.t || {}), i: Object.assign({}, served.i || {})};
  var unsaved = false;

  // Neuere Fassung aus diesem Tab (andere Seite gespeichert oder noch nicht gespeichert) hat Vorrang
  try {
    var s = JSON.parse(sessionStorage.getItem(STASH) || 'null');
    if (s && s.rev > ov.rev) { ov = {rev: s.rev, t: s.t || {}, i: s.i || {}}; unsaved = !s.saved; }
  } catch (e) {}

  function apply() {
    Object.keys(ov.t).forEach(function (k) {
      var el = document.querySelector('[data-e="' + k + '"]');
      if (el && el.textContent !== ov.t[k]) el.textContent = ov.t[k];
      if (el) el.setAttribute('data-w-changed', '');
    });
    Object.keys(ov.i).forEach(function (k) {
      var el = document.querySelector('[data-img="' + k + '"]');
      if (el) { el.src = ov.i[k]; el.removeAttribute('srcset'); el.setAttribute('data-w-changed', ''); }
    });
  }
  apply();

  var art = null, assets = null, editing = false, saving = false, readOnly = false, timer = null, target = null;
  var test = /[?&]wtest\b/.test(location.search);

  // ---------- Oberflaeche ----------
  var css = document.createElement('style');
  css.textContent = [
    '#w-bar{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:90;',
    'display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;justify-content:center;max-width:calc(100% - 32px);',
    'background:#14243F;color:#F6F3EC;border-radius:999px;padding:.45rem .5rem .45rem 1.1rem;',
    'box-shadow:0 18px 40px -16px rgba(0,0,0,.55);font:500 .85rem/1.3 Karla,"Helvetica Neue",Arial,sans-serif}',
    '#w-bar[hidden]{display:none!important}',
    '#w-status{color:#C9D3E4;display:flex;align-items:center;gap:.45rem}',
    '#w-status i{width:.5rem;height:.5rem;border-radius:50%;background:#5E9C76;display:inline-block}',
    '#w-status[data-s=dirty] i,#w-status[data-s=busy] i{background:#D0AC6A}',
    '#w-status[data-s=busy] i{animation:wpulse 1s ease-in-out infinite}',
    '#w-status[data-s=ro] i{background:#9AA5BA}',
    '@keyframes wpulse{50%{opacity:.3}}',
    '#w-bar button{font:inherit;font-weight:600;border-radius:999px;padding:.45rem 1rem;cursor:pointer;border:1px solid rgba(255,255,255,.3);background:transparent;color:#F6F3EC}',
    '#w-bar button.w-main{background:#C9A76B;border-color:#C9A76B;color:#14243F}',
    '#w-bar button:disabled{opacity:.4;cursor:default}',
    '#w-bar button:focus-visible,#w-chip:focus-visible{outline:2px solid #D0AC6A;outline-offset:2px}',
    '#w-hint{flex-basis:100%;text-align:center;font-size:.74rem;color:#9AA5BA;padding:0 .6rem .1rem}',
    'body.w-edit [data-e]{outline:1px dashed rgba(168,125,58,.45);outline-offset:3px;border-radius:3px;cursor:text}',
    'body.w-edit [data-e]:hover{outline-color:#A87D3A;background:rgba(201,167,107,.12)}',
    'body.w-edit [data-e]:focus{outline:2px solid #A87D3A;background:rgba(201,167,107,.16)}',
    'body.w-edit [data-e][data-w-changed]{box-shadow:inset 3px 0 0 #A87D3A}',
    'body.w-edit .hero-gradient,body.w-edit .sect-tint{pointer-events:none}',
    'body.w-edit img[data-img]:hover{outline:3px solid #C9A76B;outline-offset:-3px}',
    'body.w-edit .reveal{opacity:1!important;transform:none!important}',
    '#w-chip{position:fixed;z-index:91;font:600 .78rem/1 Karla,"Helvetica Neue",Arial,sans-serif;background:#C9A76B;color:#14243F;',
    'border:0;border-radius:999px;padding:.5rem .85rem;cursor:pointer;box-shadow:0 8px 20px -8px rgba(0,0,0,.5)}',
    '#w-chip[hidden]{display:none!important}'
  ].join('');
  document.head.appendChild(css);

  var bar = document.createElement('div');
  bar.id = 'w-bar'; bar.hidden = true;
  bar.innerHTML = '<span id="w-status"><i></i><span id="w-status-t"></span></span>'
    + '<button type="button" id="w-edit" class="w-main">Bearbeiten</button>'
    + '<button type="button" id="w-save" hidden>Speichern</button>'
    + '<span id="w-hint" hidden>Text anklicken und tippen &middot; Bild &uuml;berfahren oder antippen, dann &bdquo;Bild ersetzen&ldquo;</span>';
  document.body.appendChild(bar);

  var chip = document.createElement('button');
  chip.type = 'button'; chip.id = 'w-chip'; chip.hidden = true; chip.textContent = 'Bild ersetzen';
  document.body.appendChild(chip);

  var file = document.createElement('input');
  file.type = 'file'; file.accept = 'image/*'; file.id = 'w-file'; file.hidden = true;
  document.body.appendChild(file);

  var $ = function (id) { return document.getElementById(id); };

  function status(msg, s) {
    var st = $('w-status'), t = $('w-status-t');
    if (!st) return;
    if (!msg) {
      if (readOnly) { s = 'ro'; msg = 'Nur ansehen'; }
      else if (saving) { s = 'busy'; msg = 'Wird gespeichert …'; }
      else if (unsaved) { s = 'dirty'; msg = 'Ungespeicherte Änderungen'; }
      else { s = 'ok'; msg = Object.keys(ov.t).length + Object.keys(ov.i).length ? 'Alles gespeichert' : 'Werkstatt'; }
    }
    st.setAttribute('data-s', s || 'ok'); t.textContent = msg;
    $('w-save').disabled = saving || readOnly || !unsaved;
  }

  function stash(saved) {
    try { sessionStorage.setItem(STASH, JSON.stringify({rev: ov.rev, t: ov.t, i: ov.i, saved: !!saved})); } catch (e) {}
  }

  function changed() {
    ov.rev = Date.now(); unsaved = true; stash(false); status();
    clearTimeout(timer); timer = setTimeout(save, 5000);
  }

  // ---------- Bearbeiten ----------
  var plain = (function () { var d = document.createElement('div'); d.contentEditable = 'plaintext-only'; return d.contentEditable === 'plaintext-only'; })();

  function setEditing(on) {
    editing = on;
    document.body.classList.toggle('w-edit', on);
    document.querySelectorAll('[data-e]').forEach(function (el) {
      if (on) { el.setAttribute('contenteditable', plain ? 'plaintext-only' : 'true'); el.setAttribute('spellcheck', 'true'); }
      else el.removeAttribute('contenteditable');
    });
    $('w-edit').textContent = on ? 'Fertig' : 'Bearbeiten';
    $('w-edit').classList.toggle('w-main', !on);
    $('w-save').hidden = !on;
    $('w-save').classList.toggle('w-main', on);
    $('w-hint').hidden = !on;
    if (!on) { chip.hidden = true; if (unsaved) save(); }
    status();
  }

  document.addEventListener('input', function (e) {
    var el = e.target.closest && e.target.closest('[data-e]');
    if (!editing || !el) return;
    ov.t[el.getAttribute('data-e')] = el.innerText.replace(/\n+$/, '');
    el.setAttribute('data-w-changed', '');
    changed();
  });

  // Links und Aufklapp-Fragen im Bearbeiten-Modus nicht ausloesen, wenn man in ihren Text klickt
  document.addEventListener('click', function (e) {
    if (!editing) return;
    if (e.target.closest('#w-bar,#w-chip')) return;
    var ed = e.target.closest('[data-e]');
    if (ed) {
      var a = e.target.closest('a'); if (a) e.preventDefault();
      if (ed.tagName === 'SUMMARY') e.preventDefault();
      return;
    }
    // Antippen auf Bildflaechen (auch unter Verlaeufen) zeigt den Ersetzen-Knopf
    var img = imageAt(e.clientX, e.clientY);
    if (img) { e.preventDefault(); showChip(img); }
  }, true);

  document.addEventListener('keydown', function (e) {
    if (!editing) return;
    var ed = e.target.closest && e.target.closest('[data-e]');
    if (ed && e.key === 'Enter' && /^(H1|H2|H3|H4|SUMMARY|A|SPAN|DT|DD|LI)$/.test(ed.tagName)) e.preventDefault();
    if ((e.metaKey || e.ctrlKey) && e.key === 's') { e.preventDefault(); save(); }
  });

  function imageAt(x, y) {
    var els = document.elementsFromPoint ? document.elementsFromPoint(x, y) : [];
    for (var i = 0; i < els.length; i++) {
      if (els[i].matches && els[i].matches('img[data-img]')) return els[i];
      if (els[i].closest && els[i].closest('[data-e]')) return null;
    }
    return null;
  }

  function showChip(img) {
    target = img;
    var r = img.getBoundingClientRect();
    var top = Math.max(r.top + 12, 72), left = Math.min(r.right - 12, window.innerWidth - 16);
    chip.hidden = false;
    chip.style.top = top + 'px';
    chip.style.left = (left - chip.offsetWidth) + 'px';
  }

  var moveRaf = 0;
  document.addEventListener('mousemove', function (e) {
    if (!editing || moveRaf) return;
    moveRaf = requestAnimationFrame(function () {
      moveRaf = 0;
      if (e.target.closest && e.target.closest('#w-chip,#w-bar')) return;
      var img = imageAt(e.clientX, e.clientY);
      if (img) showChip(img); else chip.hidden = true;
    });
  });
  window.addEventListener('scroll', function () { chip.hidden = true; }, {passive: true});

  chip.addEventListener('click', function () {
    if (!assets) { status('Bilder ersetzen geht in dieser Ansicht nicht', 'ro'); return; }
    file.value = ''; file.click();
  });

  file.addEventListener('change', function () {
    var f = file.files && file.files[0];
    if (!f || !target || !assets) return;
    var img = target;
    status('Bild wird hochgeladen …', 'busy');
    assets.upload(f).then(function (res) {
      img.src = res.url; img.removeAttribute('srcset');
      img.setAttribute('data-w-changed', '');
      ov.i[img.getAttribute('data-img')] = res.url;
      chip.hidden = true;
      changed();
    }, function (err) {
      var c = err && err.code;
      status(c === 'too_large' ? 'Das Bild ist zu groß (max. 20 MB)' : 'Hochladen hat nicht geklappt', 'dirty');
    });
  });

  // ---------- Speichern ----------
  function save() {
    clearTimeout(timer);
    if (!unsaved || saving || readOnly) return;
    if (!art) { status('Speichern geht in dieser Ansicht nicht', 'ro'); return; }
    saving = true; status();
    var body = 'window.W_OVERRIDES=' + JSON.stringify(ov).replace(/</g, '\\u003c') + ';\n';
    art.publish({'overrides.js': {content: body, contentType: 'text/javascript'}}).then(function () {
      saving = false; unsaved = false; stash(true); status();
    }, function (err) {
      saving = false;
      var c = err && err.code;
      if (c === 'conflict') { stash(false); return; } // Ansicht laedt neu, Aenderungen kommen aus dem Zwischenspeicher zurueck
      if (/^(not_writer|not_granted|not_declared|consent_required|capability_disabled|capability_removed)$/.test(c)) {
        readOnly = true; setEditing(false); $('w-edit').hidden = true; status();
        return;
      }
      status(c === 'rate_limited' ? 'Kurz warten, dann nochmal speichern' : 'Speichern hat nicht geklappt, gleich nochmal versuchen', 'dirty');
    });
  }

  $('w-edit').addEventListener('click', function () { setEditing(!editing); });
  $('w-save').addEventListener('click', save);
  window.addEventListener('beforeunload', function () { if (unsaved) stash(false); });

  function ready() { bar.hidden = false; status(); }

  var use = window.claude && typeof window.claude.use === 'function' ? window.claude.use.bind(window.claude) : null;
  if (use) {
    use('artifact').then(function (x) { art = x; if (x) ready(); });
    use('assets').then(function (x) { assets = x; });
  }
  if (test) ready();
})();
