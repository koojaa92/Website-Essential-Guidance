# Hinweise für Änderungen an dieser Website

- Abstände zwischen den Bereichen (Sections) immer eng halten, nicht großzügig. Globale Regel am Ende von `styles.css`.
- Bei Änderungen an `styles.css` oder `main.js` die Versionsnummer (`?v=...`) in allen HTML-Dateien hochzählen, sonst zeigen Browser die alte Datei.
- Änderungen immer erst am Desktop (1280px) und Handy (390px) prüfen.
- Alle Mail-Links (mailto) gehen an essential-guidance@posteo.de, nicht an hallo@essential-guidance.de.
- FAQ-Texte (details/summary) sind zusätzlich als FAQPage-JSON-LD im <head> hinterlegt; bei FAQ-Änderungen beides angleichen.
- Der Name heißt immer "Essenz Raum" (zwei Wörter, beide groß) in allen sichtbaren Texten. Dateiname essenzraum.html und URLs bleiben unverändert.
- Termine ändern: nur `tools/termine.json` bearbeiten (Eintrag pro Termin: datum, art dance/raum/pause, optional tickets = Eventfrog-Link, optional hinweis bei Pause), danach `python3 tools/make-ics.py` ausführen. Das Tool baut die Terminkarten in termine/index/essential-dance/essenzraum.html, die Kalenderdateien und die Event-Daten für Google. Karten nie direkt im HTML ändern. Ohne Ticketlink zeigt die Karte „Tickets folgen“.
- FAQ-Abschnitte haben immer grauen Hintergrund (`<section class="tint">`).
- Live ist der Branch `main` (GitHub Pages).

## Marke und SEO (verbindlich)
- Essential Guidance = Dachmarke. Darunter drei eigenständige Bereiche: Essential Dance (Tanzmarke), Essenz Raum (Tagesformat), Einzelbegleitung.
- "Ecstatic Dance" nur als beschreibender Begriff ("inspiriert von Ecstatic Dance"), nie als Markenname. "Ecstatic Dance Freiburg" ist der Name eines anderen Anbieters (freitags) und darf nicht in Titeln oder Event-Namen stehen.
- Alleinstellung im Freiburger Umfeld: Essential Dance ist sonntags (Ecstatic Dance Freiburg und 5Rhythmen freitags, Holy Wild/Take5 samstags).
- Ort immer gleich schreiben: Studio Pro Arte, Am Rohrgraben 4a, 79249 Merzhausen bei Freiburg.
- llms.txt ist die Kurzbeschreibung für KI-Systeme; bei Preis-, Zeit- oder Angebotsänderungen mitpflegen.
- Domain: Ziel ist essential-guidance.de (Strato). Umstellung erst, wenn der DNS-Eintrag bei Strato auf GitHub Pages zeigt; dann in allen Dateien (HTML, sitemap.xml, robots.txt, llms.txt, tools/make-ics.py, CNAME) essential-guidance.space durch essential-guidance.de ersetzen, Datenschutz-Abschnitt "Domain" anpassen und .space bei Cloudflare per 301 auf .de umleiten.
- Impressum: Umsatzsteuer-Abschnitt liegt als HTML-Kommentar mit Platzhalter bereit; aktivieren, sobald Jakob die Angabe liefert. Keine Nummern erfinden.
- Statistik: GoatCounter (cookielos), Konto `essentialgoat`, eingebunden in main.js und in datenschutz.html beschrieben. Auswertung: https://essentialgoat.goatcounter.com
