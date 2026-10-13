# Essential Guidance – Projektstand und offene Punkte

Stand: 6. Oktober 2026 (Mittag). Live: https://essential-guidance.space (Branch `main`, GitHub Pages).
Technische Regeln für Änderungen stehen in `CLAUDE.md`.


## Was steht (Kurzfassung)

**Marke und Positionierung**
- Essential Guidance = Dach. Darunter Essential Dance (Tanz, Hauptangebot), Essenz Raum (Workshop), Einzelbegleitung.
- Essential Dance ist „inspiriert von Ecstatic Dance“, nie „Ecstatic Dance Freiburg“ (das ist ein anderer Anbieter, freitags).
- Alleinstellung: sonntags. Ort: Studio Pro Arte, Am Rohrgraben 4a, 79249 Merzhausen bei Freiburg.
- „Coaching“ wird nicht als Selbstbezeichnung verwendet (KSK). Nur verneinend in FAQs.

**Startseite**
- Slogan „Raum für deine Essenz.“, darunter „Tanz · Workshops · Einzelbegleitung in Freiburg“.
- Neue Sektion „Was ist Essential Guidance?“ vor den Terminen.
- Goldzeilen beginnen mit der Art: Tanz / Workshop / 1:1.
- Einzelbegleitung: „Ein Gespräch, ein Bild, ein nächster Schritt.“ mit Beschreibung des Live-Zeichnens.
- „Höre meinen Sound“ führt zu SoundCloud. Sonnenfoto dezent hinter „Bleib in Verbindung“ und Footer.
- „Nächster Termin“ springt ab 21 Uhr auf den folgenden Termin.
- Die drei Angebote füllen am Handy je einen Bildschirm. Am Desktop stehen sie als klare Blöcke mittig, die Nachbarn schauen schmal herein; Bild an Bildschirmhöhe gebunden, größere Schrift, sanftes Einrasten (6.10., Mittelweg; Regel am Ende von styles.css).

**Unterseiten**
- Essenz Raum: Reihenfolge Intro, ein blauer Block aus „Der Tag“ und „Was den Essenz Raum ausmacht“ (Kartentexte aus Sicht der Lesenden), dann drei Spalten „Wie ich den Raum halte“ · „Was kannst du mitnehmen?“ · „Wann ist er nichts für dich?“, Termine (nur die nächsten drei), FAQ. Preis-Hinweis steht unter den Terminen. Im Hero „Workshop in kleiner Gruppe“, Ort mit Kartenlink.
- Essential Dance: Preise „ab 15 € VVK · ab 20 € Abendkasse“, FAQs mit Suchbegriffen, „DJ Bookings“ als goldene Überzeile.
- Einzelbegleitung: „Mit was ich arbeite“, Gene Keys als goldene Überzeile.
- Über mich: ohne Kontaktblock, weißer Abstand vor „Meine Vision“. Mit „zehn Jahre selbstständig als Graphic Recorder und Facilitator“ und „Vater einer lebendigen Tochter, die mich immer wieder aufs Neue prüft“.

**Termine**
- Alle Termine in `tools/termine.json`. Danach `python3 tools/make-ics.py` ausführen: Das baut Karten, Kalenderdateien und Google-Daten.
- 2026: bis 20.12. mit Eventfrog-Links. 2027: Essential Dance 17.1.–21.3. (ohne 28.3.), Essenz Raum 31.1. Dort steht „Tickets folgen“.

**Linkseite (QR-Code / Instagram-Bio)**
- `links.html`: versteckte Linkseite (noindex, nicht im Menü, nicht in der Sitemap) mit Terminen, den drei Angeboten, Telegram, SoundCloud, Instagram, E-Mail und Website. QR-Code: `_projekt/qr-links.png` und `.svg` (zeigt auf essential-guidance.space/links.html, funktioniert nach dem Domainwechsel über die Weiterleitung weiter).

**Technik und SEO**
- Google Search Console eingerichtet, Sitemap eingereicht, Seite ist bei Google indexiert (2.10.).
- Event-Daten für Google mit validFrom ergänzt. Die Prüfung in der Search Console läuft seit 4.10.
- Strukturierte Daten: Organisation, Person, Essential Dance, Events, FAQs. llms.txt für KI-Systeme.
- Statistik: GoatCounter (cookielos), https://essentialgoat.goatcounter.com
- jakob-kohlbrenner.de verlinkt auf die neue Seite.
- Cloudflare „Always Use HTTPS“ eingeschaltet (13.10.): http und www leiten per 301 auf https://essential-guidance.space weiter. HSTS bewusst aus (wegen späterem Wechsel auf .de).

**Entscheidungen aus der Design-Kritik (7.10.)**
- Startseite ohne Preise, sechs Termine, keine Erstbesucher-Zeile; „Was ist Essential Guidance?“ bleibt bewusst textlastig.
- Fußzeile ohne Straßenadresse (Studio Pro Arte ist nicht Jakobs Adresse).
- Umgesetzt: Ticket-Pillen mit dunkler Schrift, größere Datumszeile am Handy, Hero-Button „Termine ansehen“ in Gold, Essenz-Raum-Kartenbild am Handy nach links verschoben, Menü wird offen zum X, goldene Schlusszeile beim Essenz Raum auf der Startseite.

## Offene Punkte

### Als Nächstes (Jakob, Stand 13.10.)
1. [x] **Bing Webmaster Tools** eingerichtet (13.10.). Noch: Sitemap einreichen und drei URLs übermitteln, falls nicht geschehen.
2. [ ] **Cloudflare**: „AI Crawl Control“ ansehen (Screenshot an Claude) und „Crawler Hints“ einschalten.
3. [ ] **Google-Unternehmensprofil** anlegen (als Anbieter mit Einzugsgebiet, siehe unten).
4. [ ] **Brevo-Newsletter** einrichten (Double-Opt-in, Datenschutz anpassen, siehe „Später“).
5. [ ] **Domain .de** umziehen (Schritte siehe „Bald“), dazu optional essential-dance.de als Weiterleitung.


### Bald
- [ ] **Echte Fotos** für Essential Dance und Essenz Raum (liefert Jakob). Ziel: beide Formate in Farbe und Bildwelt klar unterscheidbar.
- [ ] **Domain .de**: Bei Strato A-Einträge `185.199.108.153` (bis .111.153) und CNAME `www` → `koojaa92.github.io` setzen, dann Claude Bescheid geben. Danach: .space in Cloudflare per 301 auf .de umleiten, .de in der Search Console anlegen und dort „Adressänderung“ ausführen. Links bei Instagram, Eventfrog und jakob-kohlbrenner.de anpassen.
- [x] Eventfrog: Website-Link ist in den Events eingetragen (13.10.). Jakob lässt es so.
- [ ] **Eventfrog Newsletter-Häkchen**: Nur bei Events ohne bisherige Verkäufe auf Plus umstellen (Gebühr an Käufer weitergeben), Ja/Nein-Feld freiwillig.
- [ ] **Instagram-Bio** mit den drei Angeboten und Website-Link (wichtig).
- [x] **Cloudflare geprüft (13.10.)**: Die Seite läuft über Cloudflare (Proxy aktiv, Antworten kommen von „server: cloudflare“). Der Cloudflare-Satz in der Datenschutzerklärung bleibt also drin.
- [ ] **Search Console**: Prüfung „validFrom“ abwarten. Bei Fehler einen Screenshot an Claude.

### Stand Größen und Layout (9.–13.10.)
- Desktop: ganze Website in gleicher Proportion größer (Grundgröße wächst mit Bildschirm, max. ca. +30 %). Kopfzeile, Fuß und Abstände zwischen Abschnitten bleiben bewusst kleiner/eng. Handy unverändert, außer Startbild (Textblock kompakt und tief im Bild).
- Startseite: Regenbogenbild unter „Was ist Essential Guidance?“ mit weißem Verlauf (Jakob gefällt es). Termine-Seite: vier Karten pro Reihe.
- [ ] **Entscheidung offen**: Am Desktop ragen Essenz Raum („Der Tag“), „Formen der Begleitung“ und Gene Keys über einen Bildschirm hinaus. Vorschlag: Bilder und Innenabstände verkleinern, Gene Keys scrollen lassen.
- [ ] **Entscheidung offen**: Größere Handy-Terminkarten (Vorschau in `_projekt/vorschau-handy-termine.png`).
- [ ] Höher aufgelöstes Original des Regenbogenfotos (jetzt nur 1052 × 848 px) – falls vorhanden, an Claude.

### Gefunden werden: Stand 13.10.
- Search Console: Sitemap ok (8 Seiten). Indexiert: Startseite, Essential Dance, Über mich, Einzelbegleitung, Impressum. Für Essenz Raum, Termine, Einzelbegleitung am 13.10. „Indexierung beantragt“. In ca. 1 Woche bei Google `site:essential-guidance.space` prüfen.
- Ziel-Suchbegriff: **„Essential Dance“** (eigener Name, dort ist Jakob der einzige echte Anbieter). „Ecstatic Dance Freiburg“ ist Name und Domain eines anderen Anbieters, dort nicht um Platz 1 kämpfen.
- [x] **Website (13.10.)**: Titel „Essential Dance · Freies Tanzen sonntags in Freiburg“, „Essential Dance“ in der Hauptüberschrift (für Google, optisch gleich), Marke mit Instagram, SoundCloud, Telegram verknüpft. Eventfrog hat keine eigene Veranstalter-Profilseite; dort steht als Veranstalter „Jakob Kohlbrenner“ mit Website-Link.
- [ ] **Bing Webmaster Tools**: bing.com/webmasters, „Aus Google Search Console importieren“, danach Sitemap prüfen und Startseite per „URL-Übermittlung“ einreichen.
- [ ] **Cloudflare**: „AI Crawl Control“ prüfen (KI-Such-Crawler zulassen) und unter Caching → Konfiguration „Crawler Hints“ einschalten (meldet Änderungen automatisch an Bing).
- llms.txt um Kurz-FAQ für KI-Suche ergänzt (13.10.), u. a. „sonntags frei tanzen“, „Ecstatic Dance am Sonntag“, „Conscious Dance“.
- [ ] **Name überall gleich „Essential Dance“ mit Link**: Eventfrog-Veranstalter und alle Events, Instagram-Namensfeld „Essential Dance · Jakob Kohlbrenner“ plus Link, SoundCloud, Telegram, ecstaticdance.org, Studio Pro Arte.
- [ ] **Domain essential-dance.de** ist frei (13.10.), ebenso essential-dance-freiburg.de. Bei Strato registrieren und nur als Weiterleitung auf die Essential-Dance-Seite nutzen, keine zweite Website. essentialdance.de (ohne Bindestrich) ist geparkt/vergeben, ignorieren.
- [ ] Nach 3–4 Wochen in der Search Console unter „Leistung“ die echten Suchbegriffe ansehen, dann über weitere Begriffe entscheiden („Tanzabend Freiburg“, „Tanzen ohne Partner“).

### Inhalte
- [ ] **Einzelbegleitung-Seite**: Einstieg schärfen, das Live-Zeichnen an den Anfang. Claude schickt einen Textvorschlag.
- Erledigt: Längerer Text „Was ist Essential Guidance?“ auf der Startseite (freigegeben am 6.10.).
- [ ] **Bild für „Was ist Essential Guidance?“** auswählen (Vorschläge: Keimling, Feldweg, Porträt). Abschnitt soll am Handy auf einen Bildschirm passen.
- Entschieden (7.10., nach Impeccable-Critique): Keine Preise auf der Startseite. „Was ist Essential Guidance?“ bleibt bewusst textlastig. Sechs Termine auf der Startseite (Hauptfunktion). Kein Erstbesucher-Hinweis nötig (Publikum kennt Tanz). Footer-Ort ohne Straße, weil Studio Pro Arte nicht Jakobs Adresse ist.
- Entschieden: Die Startseite zeigt am Handy weiter alle Termine, damit der Essenz Raum immer sichtbar ist und man den Überblick behält.
- Entschieden: Die Kachelbilder der Einzelbegleitung bleiben farbig (sie sind schon leicht entsättigt, der Regenbogen bei „Innere Anteile“ trägt Bedeutung). Eventuell sucht Jakob konsistentere Bilder.
- Erledigt (6.10.): Über-mich-Überschrift „Die Essenz zu erforschen ist mein Weg.“
- [ ] **Über mich, Hero-Bild**: ein Bild, auf dem Jakob mit Menschen im Kontext zu sehen ist (nicht tanzend), zum Beispiel beim Halten eines Kreises oder beim Graphic Recording. Jakob sucht ein eigenes Foto. Kein Tanzbild, nicht das Graphic-Recording-Foto. Sonst aus dem Fotoshooting.
- [ ] **Texte selbst durchlesen** und Menschen, die sich mit Texten auskennen, für ein tiefes Feedback geben.
- [ ] **Impressum**: Pflicht ist nur die Umsatzsteuer-Identifikationsnummer (USt-IdNr., beginnt mit DE), falls Jakob eine hat. Die normale Steuernummer gehört nicht ins Impressum. Ohne USt-IdNr. (z. B. als Kleinunternehmer) bleibt der Abschnitt einfach weg. Der Platzhalter liegt im Code.

### Termine 2027
- [ ] Termine im Kalender aktuell halten (`tools/termine.json`).
- [ ] Eventfrog-Events für 2027 anlegen und die Links in `tools/termine.json` eintragen lassen (Feld `tickets`).
- [ ] Pausentage 2027 festlegen.
- [ ] Weitere Essenz-Raum-Termine 2027 festlegen und bei Studio Pro Arte buchen. Überlegen, ob für den Essenz Raum zusätzlich Saal 2 gebucht wird.
- [ ] Essenz Raum über Eventfrog verkaufen. Ab 50 € braucht das Plus. Danach die Website von Mail-Anmeldung auf Eventfrog umstellen.

### SEO und Auffindbarkeit
- [ ] Search Console alle paar Wochen anschauen: „Seiten“ (indexiert?) und „Leistung“ (Suchbegriffe).
- [ ] Google-Unternehmensprofil, Eintrag bei ecstaticdance.org, Studio Pro Arte, visit.freiburg.de (siehe unten).
- [ ] Google-Unternehmensprofil ohne eigenen Ort: als „Unternehmen mit Einzugsgebiet“ anlegen (Einzugsgebiet z. B. Freiburg und Umgebung). Die Wohnadresse dient nur zur Bestätigung und wird ausgeblendet, öffentlich ist sie nicht sichtbar. Studio Pro Arte nicht als eigene Adresse angeben, nur in den Events und Beschreibungen nennen.

### Später
- [ ] **Newsletter über Brevo** (erst nach Freigabe): Anmeldeformular mit Bestätigungsmail (Double-Opt-in), Abmeldelink in jeder Mail, Datenschutzerklärung anpassen.
- [ ] **Fotoshooting Einzelbegleitung**: sechs Motive in einem Licht und einem Format (Präsenz, Zeichnen, Innere Anteile, Gene Keys, Tempo, Raum). Eine befreundete Person als Klient, schriftliche Einwilligung.
- [ ] **Echtes Foto vom Essenz-Raum-Kreis** (wichtig), damit sich das Bild klar vom Essential-Dance-Bild unterscheidet.
- [ ] **Printflyer Essenz Raum**.
- [ ] **Logo**: eigenes Zeichen entwickeln. Der Schriftzug oben links nutzt bis dahin die Überschriften-Schrift Crimson Pro.

## Gefunden werden: was außerhalb der Website hilft

Nach Wirkung sortiert. Wenige gute Einträge sind besser als viele Verzeichnisse.

1. **Google-Unternehmensprofil** (business.google.com): stärkstes Signal für Google Maps und Suchen wie „Tanzen Freiburg“. Geht auch ohne öffentliche Adresse, als Anbieter mit Einzugsgebiet.
2. **Bing Webmaster Tools** (bing.com/webmasters): Import aus der Google Search Console mit einem Klick. Wichtig, weil ChatGPT, Copilot und andere KI-Suchen auf den Bing-Index zugreifen.
3. **ecstaticdance.org**: Eintrag im internationalen Verzeichnis. Google zeigt es schon bei „Ecstatic Dance Freiburg“.
4. **visit.freiburg.de**: Seite „Tanzen in Freiburg“, bei der FWTM nach einer Aufnahme fragen.
5. **Studio Pro Arte**: Eintrag im Kursplan mit Link.
6. **Kooperationen**: Andrea Gruner, Embodiment (Movement Medicine). Bei gemeinsamen Events um eine Nennung mit Link bitten.
7. **Regionale Veranstaltungskalender**: zum Beispiel Badische Zeitung, fudder.
8. **Apple Business Connect** (optional): wie das Google-Profil, für Apple Karten und Siri.

Was gerade im Stillen weiterwirkt: Die Seite ist indexiert, die Search Console zeigt nach ein paar Wochen unter „Leistung“, mit welchen Suchbegriffen du gefunden wirst. GoatCounter zeigt unter „Top referrers“, woher Besucher kommen.

---

Die Seite ist lebendig und muss nicht perfekt sein. Sie lebt von den Angeboten.
