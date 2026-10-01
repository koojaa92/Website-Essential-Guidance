#!/usr/bin/env python3
"""Erzeugt essential-dance.ics und essenzraum.ics aus den Terminkarten in termine.html
und schreibt die passenden Event-Daten (schema.org) in termine/essential-dance/essenzraum.html.
Aufruf im Projektordner: python3 tools/make-ics.py"""
import re, datetime as dt

SITE = 'https://essential-guidance.space'

html = open('termine.html', encoding='utf-8').read()
cards = re.findall(r'<div class="dcard( raum)?" data-date="([\d-]+)"', html)

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
              'SUMMARY:'+esc(summary),'LOCATION:'+esc('Studio Pro Arte, Freiburg'),
              'DESCRIPTION:'+esc(desc),'URL:'+SITE+'/termine.html','END:VEVENT']
        body += '\r\n'.join(fold(l) for l in ev) + '\r\n'
    return body + 'END:VCALENDAR\r\n'

ed, er = [], []
raumtage = {day for raum, day in cards if raum}
for raum, day in cards:
    if not raum:
        ed.append(('ed-'+day, day, '1700', '2000', 'Essential Dance',
          'Ecstatic Dance in Freiburg, 17-20 Uhr. 15 € VVK über Eventfrog, 20 € Abendkasse. Keine Anmeldung nötig.'
          + (' Am selben Tag findet von 11 bis 16 Uhr der Essenz Raum statt.' if day in raumtage else '')))
    else:
        er.append(('er-'+day, day, '1100', '1600', 'Essenz Raum',
          'Ein Tag in kleiner Gruppe, 11-16 Uhr. Im Anschluss Tanzen (Essential Dance) 17-20 Uhr. '
          '75 / 90 / 110 € inkl. 7 % MwSt., du wählst. Anmeldung per E-Mail an essential-guidance@posteo.de.'))
for fn, name, ev in (('essential-dance.ics','Essential Dance Freiburg',ed),('essenzraum.ics','Essenz Raum Freiburg',er)):
    open(fn,'w',encoding='utf-8',newline='').write(cal(name, sorted(ev, key=lambda e:e[1])))
    print(fn, len(ev), 'Termine')

# Strukturierte Daten (schema.org Event) für Google und KI-Suchen, aus denselben Karten
import json
links = dict(re.findall(r'data-date="([\d-]+)">.*?<a class="dcard-flag" href="(https://eventfrog[^"]+)"', html))
PLACE = {'@type': 'Place', 'name': 'Studio Pro Arte',
         'address': {'@type': 'PostalAddress', 'streetAddress': 'Am Rohrgraben 4a', 'postalCode': '79249',
                     'addressLocality': 'Merzhausen bei Freiburg', 'addressRegion': 'Baden-Württemberg', 'addressCountry': 'DE'}}
ORG = {'@type': 'Organization', 'name': 'Essential Guidance', 'url': SITE + '/'}
def ev_ld(day, kind):
    if kind == 'ed':
        return {'@type': 'DanceEvent', 'name': 'Essential Dance – Ecstatic Dance Freiburg',
                'description': 'Freies Tanzen (Ecstatic Dance) mit kuratierter Musikreise: Einstimmung im Kreis, zwei Tanzwellen, stiller Ausklang. Ohne Anmeldung.',
                'startDate': day + 'T17:00:00+' + tz(day), 'endDate': day + 'T20:00:00+' + tz(day),
                'eventStatus': 'https://schema.org/EventScheduled', 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
                'location': PLACE, 'image': SITE + '/images/img-7089e9983714.jpg', 'organizer': ORG,
                'performer': {'@type': 'Person', 'name': 'Jakob Kohlbrenner'},
                'offers': {'@type': 'Offer', 'price': '15', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock',
                           'url': links.get(day, SITE + '/termine.html')}}
    return {'@type': 'Event', 'name': 'Essenz Raum – ein Tag in kleiner Gruppe',
            'description': 'Ein Tag in kleiner Gruppe mit Bewegung, Kontemplation, Teilen und Malen. Mittagessen und Essential Dance am Abend inklusive. Anmeldung per E-Mail.',
            'startDate': day + 'T11:00:00+' + tz(day), 'endDate': day + 'T16:00:00+' + tz(day),
            'eventStatus': 'https://schema.org/EventScheduled', 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
            'location': PLACE, 'image': SITE + '/images/img-262a22e84b99.jpg', 'organizer': ORG,
            'offers': {'@type': 'Offer', 'price': '75', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock',
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
