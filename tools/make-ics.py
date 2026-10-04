#!/usr/bin/env python3
"""Baut alle Termine aus tools/termine.json:
- Terminkarten in termine.html, index.html, essential-dance.html, essenzraum.html
- Kalenderdateien essential-dance.ics und essenzraum.ics
- Event-Daten fuer Google (schema.org JSON-LD)
Termine aendern: nur tools/termine.json bearbeiten, dann im Projektordner: python3 tools/make-ics.py
Eintrag: {"datum": "JJJJ-MM-TT", "art": "dance" | "raum" | "pause", "tickets": "Eventfrog-Link" (optional),
          "hinweis": {"text": "...", "url": "..."} (optional, nur bei Pause)}"""
import re, json, datetime as dt

SITE = 'https://essential-guidance.space'
TERMINE = sorted(json.load(open('tools/termine.json', encoding='utf-8')),
                 key=lambda e: (e['datum'], {'pause': 0, 'raum': 1, 'dance': 2}[e['art']]))
TICKETS = {e['datum']: e.get('tickets') for e in TERMINE if e['art'] == 'dance'}

def esc(t): return t.replace('\\','\\\\').replace(';','\;').replace(',','\\,').replace('\n','\\n')
def fold(line):
    out, cur = [], ''
    for ch in line:
        if len((cur + ch).encode('utf-8')) > (75 if not out else 74):
            out.append(cur); cur = ch
        else:
            cur += ch
    out.append(cur)
    return '\r\n '.join(out)

TZ = ('BEGIN:VTIMEZONE\r\nTZID:Europe/Berlin\r\nBEGIN:DAYLIGHT\r\nTZOFFSETFROM:+0100\r\nTZOFFSETTO:+0200\r\n'
      'TZNAME:CEST\r\nDTSTART:19700329T020000\r\nRRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\r\nEND:DAYLIGHT\r\n'
      'BEGIN:STANDARD\r\nTZOFFSETFROM:+0200\r\nTZOFFSETTO:+0100\r\nTZNAME:CET\r\nDTSTART:19701025T030000\r\n'
      'RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\r\nEND:STANDARD\r\nEND:VTIMEZONE\r\n')

def cal(name, events):
    stamp = dt.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    L = ['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Essential Guidance//Termine//DE','CALSCALE:GREGORIAN',
         'METHOD:PUBLISH','X-WR-CALNAME:'+esc(name),'X-WR-TIMEZONE:Europe/Berlin',
         'REFRESH-INTERVAL;VALUE=DURATION:PT12H','X-PUBLISHED-TTL:PT12H']
    body = '\r\n'.join(fold(l) for l in L) + '\r\n' + TZ
    for uid, day, start, end, summary, desc in events:
        d = day.replace('-','')
        ev = ['BEGIN:VEVENT','UID:'+uid+'@essential-guidance.space','DTSTAMP:'+stamp,
              f'DTSTART;TZID=Europe/Berlin:{d}T{start}00', f'DTEND;TZID=Europe/Berlin:{d}T{end}00',
              'SUMMARY:'+esc(summary),'LOCATION:'+esc('Studio Pro Arte, Am Rohrgraben 4a, 79249 Merzhausen bei Freiburg'),
              'DESCRIPTION:'+esc(desc),'URL:'+SITE+'/termine.html','END:VEVENT']
        body += '\r\n'.join(fold(l) for l in ev) + '\r\n'
    return body + 'END:VCALENDAR\r\n'


# ---------- Terminkarten ----------
MONATE = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
KURZ = ['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez']
TAGE = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag']
IMG = {'dance': ('images/img-7089e9983714.jpg', 'Essential Dance in Freiburg'), 'raum': ('images/img-262a22e84b99.jpg', 'Essenz Raum in Freiburg')}
MAIL_M = {'März': 'M%C3%A4rz'}

def media(e):
    d = dt.date.fromisoformat(e['datum'])
    big = f'<span class="dcard-big"><b>{d.day}</b> <i><span class="m-voll">{MONATE[d.month-1]}</span><span class="m-kurz">{KURZ[d.month-1]}</span></i></span>'
    if e['art'] == 'pause':
        return f'<div class="dcard-media"><div class="dcard-img pause-fill"></div>{big}</div>'
    src, alt = IMG[e['art']]
    return f'<div class="dcard-media"><img loading="lazy" decoding="async" class="dcard-img" src="{src}" alt="{alt}">{big}</div>'

def datum(e):
    d = dt.date.fromisoformat(e['datum'])
    return f'{TAGE[d.weekday()]}, {d.day}. {MONATE[d.month-1]}'

def anmeldung(e):
    d = dt.date.fromisoformat(e['datum']); m = MONATE[d.month-1]
    return ('<a class="dcard-flag" href="mailto:essential-guidance@posteo.de?subject=Anmeldung%20Essenz%20Raum&amp;body='
            'Hallo%20Jakob%2C%0A%0Aich%20m%C3%B6chte%20mich%20gerne%20f%C3%BCr%20den%20Essenz%20Raum%20am%20'
            f'{d.day}.%20{MAIL_M.get(m, m)}%20anmelden.%0A%0AHerzliche%20Gr%C3%BC%C3%9Fe%0A%28Name%29">Anmeldung</a>')

def tickets(e):
    if e.get('tickets'):
        return f'<a class="dcard-flag" href="{e["tickets"]}" target="_blank" rel="noopener">Tickets</a>'
    return '<span class="dcard-folgt">Tickets folgen</span>'

def karte(e, seite):
    art, cls = e['art'], {'dance': 'dcard', 'raum': 'dcard raum', 'pause': 'dcard pause'}[e['art']]
    if art == 'pause':
        h = e.get('hinweis')
        text = 'An diesem Sonntag findet kein Essential Dance statt.' + (' Du findest mich hier:' if h else '')
        foot = f'<div class="dcard-foot"><a class="dcard-link" href="{h["url"]}" target="_blank" rel="noopener">{h["text"]} &rarr;</a></div>' if h else ''
        body = f'<div class="dcard-date">{datum(e)}</div><h3>Pause</h3><p>{text}</p>{foot}'
    elif art == 'dance':
        preis = '<p class="dcard-preis">ab 15 &euro; VVK &middot; ab 20 &euro; Abendkasse</p>' if seite == 'ed' else ''
        details = 'termine.html' if seite == 'ed' else 'essential-dance.html'
        body = (f'<div class="dcard-date">{datum(e)}</div><h3>Essential Dance</h3><p>17&ndash;20 Uhr</p>{preis}'
                f'<div class="dcard-foot">{tickets(e)}<a class="dcard-link" href="{details}">Details</a></div>')
    else:
        if seite == 'ez':
            body = (f'<div class="dcard-date">{datum(e)}</div><h3>Essenz Raum</h3><p>11&ndash;16 Uhr &middot; danach Tanzen 17&ndash;20 Uhr</p>'
                    f'<p class="dcard-preis">90 &euro;</p><div class="dcard-foot">{anmeldung(e)}</div>')
        else:
            body = (f'<div class="dcard-date">{datum(e)}</div><h3>Essenz Raum</h3><p>11&ndash;16 Uhr</p>'
                    f'<div class="dcard-foot">{anmeldung(e)}<a class="dcard-link" href="essenzraum.html">Details</a></div>')
    return f'<div class="{cls}" data-date="{e["datum"]}">{media(e)}<div class="dcard-body">{body}</div></div>'

SEITEN = [('termine.html', 'dates-all', 'termine', {'dance', 'raum', 'pause'}, True),
          ('index.html', 'dates-home', 'home', {'dance', 'raum'}, False),
          ('essential-dance.html', 'dates-ed', 'ed', {'dance'}, False),
          ('essenzraum.html', 'dates-ez', 'ez', {'raum'}, False)]
for fn, cid, seite, arten, jahre in SEITEN:
    out, jahr = [], TERMINE[0]['datum'][:4]
    for e in TERMINE:
        if e['art'] not in arten: continue
        if jahre and e['datum'][:4] != jahr:
            jahr = e['datum'][:4]; out.append(f'<div class="dates-jahr">{jahr}</div>')
        out.append(karte(e, seite))
    s = open(fn, encoding='utf-8').read()
    m = re.search(r'(<div class="dates" id="' + cid + r'"[^>]*>\n)(.*?)(\n    </div>\n)', s, re.S)
    assert m, fn
    s = s[:m.start(2)] + '\n'.join('      ' + c for c in out) + s[m.end(2):]
    open(fn, 'w', encoding='utf-8').write(s)
print('Terminkarten in termine, index, essential-dance, essenzraum aktualisiert')

# ---------- Kalenderdateien ----------
ed, er = [], []
raumtage = {e['datum'] for e in TERMINE if e['art'] == 'raum'}
for e in TERMINE:
    day = e['datum']
    if e['art'] == 'dance':
        ed.append(('ed-'+day, day, '1700', '2000', 'Essential Dance',
          'Freies Tanzen in Freiburg, 17-20 Uhr. Ab 15 € VVK über Eventfrog, ab 20 € Abendkasse. Keine Anmeldung nötig.'
          + (' Am selben Tag findet von 11 bis 16 Uhr der Essenz Raum statt.' if day in raumtage else '')))
    elif e['art'] == 'raum':
        er.append(('er-'+day, day, '1100', '1600', 'Essenz Raum',
          'Ein Tag in kleiner Gruppe, 11-16 Uhr. Im Anschluss Tanzen (Essential Dance) 17-20 Uhr. '
          '90 €, Mittagessen und Essential Dance am Abend inklusive. Anmeldung per E-Mail an essential-guidance@posteo.de.'))
for fn, name, ev in (('essential-dance.ics','Essential Dance Freiburg',ed),('essenzraum.ics','Essenz Raum Freiburg',er)):
    open(fn,'w',encoding='utf-8',newline='').write(cal(name, ev))
    print(fn, len(ev), 'Termine')

# ---------- Event-Daten fuer Google ----------
PLACE = {'@type': 'Place', 'name': 'Studio Pro Arte',
         'address': {'@type': 'PostalAddress', 'streetAddress': 'Am Rohrgraben 4a', 'postalCode': '79249',
                     'addressLocality': 'Merzhausen bei Freiburg', 'addressRegion': 'Baden-Württemberg', 'addressCountry': 'DE'}}
ORG = {'@type': 'Organization', 'name': 'Essential Guidance', 'url': SITE + '/'}
def ev_ld(day, kind):
    if kind == 'ed':
        return {'@type': 'DanceEvent', 'name': 'Essential Dance – freies Tanzen am Sonntag in Freiburg',
                'description': 'Freies Tanzen ohne Schritte, inspiriert von Ecstatic Dance, mit DJ-Musikreise: Einstimmung im Kreis, zwei Tanzwellen, stiller Ausklang. Ohne Anmeldung.',
                'startDate': day + 'T17:00:00+' + tz(day), 'endDate': day + 'T20:00:00+' + tz(day),
                'eventStatus': 'https://schema.org/EventScheduled', 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
                'location': PLACE, 'image': SITE + '/images/img-7089e9983714.jpg', 'organizer': ORG,
                'performer': {'@type': 'Person', 'name': 'Jakob Kohlbrenner', 'url': SITE + '/ueber.html'},
                'offers': {'@type': 'Offer', 'price': '15', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock', 'validFrom': '2026-10-01T00:00:00+02:00',
                           'url': TICKETS.get(day) or SITE + '/termine.html'}}
    return {'@type': 'Event', 'name': 'Essenz Raum – Workshop in kleiner Gruppe',
            'description': 'Ein Tag in kleiner Gruppe mit Bewegung, Kontemplation, Teilen und Malen. Mittagessen und Essential Dance am Abend inklusive. Anmeldung per E-Mail.',
            'startDate': day + 'T11:00:00+' + tz(day), 'endDate': day + 'T16:00:00+' + tz(day),
            'eventStatus': 'https://schema.org/EventScheduled', 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
            'location': PLACE, 'image': SITE + '/images/img-262a22e84b99.jpg', 'organizer': ORG,
            'offers': {'@type': 'Offer', 'price': '90', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock', 'validFrom': '2026-10-01T00:00:00+02:00',
                       'url': SITE + '/essenzraum.html'}}
def tz(day):  # Sommerzeit bis letzter Sonntag im Oktober
    d = dt.date.fromisoformat(day)
    def last_sun(m): x = dt.date(d.year, m, 31); return x - dt.timedelta(days=(x.weekday() + 1) % 7)
    return '02:00' if last_sun(3) <= d < last_sun(10) else '01:00'
def inject(fn, items):
    s = open(fn, encoding='utf-8').read()
    block = ('<script type="application/ld+json" id="events-ld">'
             + json.dumps({'@context': 'https://schema.org', '@graph': items}, ensure_ascii=False) + '</script>')
    s = re.sub(r'<script type="application/ld\+json" id="events-ld">.*?</script>\n?', '', s, flags=re.S)
    s = s.replace('</head>', block + '\n</head>', 1)
    open(fn, 'w', encoding='utf-8').write(s)
EDL = [ev_ld(e[1], 'ed') for e in sorted(ed, key=lambda e: e[1])]
ERL = [ev_ld(e[1], 'er') for e in sorted(er, key=lambda e: e[1])]
inject('termine.html', sorted(EDL + ERL, key=lambda e: e['startDate']))
inject('essential-dance.html', EDL)
inject('essenzraum.html', ERL)
print('Event-Daten in termine.html, essential-dance.html, essenzraum.html aktualisiert')
