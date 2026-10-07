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

## Offene Punkte

### Bald
- [ ] **Domain .de**: Bei Strato A-Einträge `185.199.108.153` (bis .111.153) und CNAME `www` → `koojaa92.github.io` setzen, dann Claude Bescheid geben. Danach: .space in Cloudflare per 301 auf .de umleiten, .de in der Search Console anlegen und dort „Adressänderung“ ausführen. Links bei Instagram, Eventfrog und jakob-kohlbrenner.de anpassen.
- [ ] **Eventfrog-Beschreibung** mit dem neuen Text (Suchbegriffe, Website-Link) bei allen Events einsetzen. Website auch im Veranstalterprofil eintragen.
- [ ] **Eventfrog Newsletter-Häkchen**: Nur bei Events ohne bisherige Verkäufe auf Plus umstellen (Gebühr an Käufer weitergeben), Ja/Nein-Feld freiwillig.
- [ ] **Instagram-Bio** mit den drei Angeboten und Website-Link (wichtig).
- [ ] **Cloudflare prüfen**: Im Cloudflare-Konto unter DNS bei essential-guidance.space nachsehen, ob neben den Einträgen eine orange Wolke („Proxied“) oder eine graue Wolke („DNS only“) steht. Orange heißt: Die Besucher laufen über Cloudflare, dann muss der Satz in der Datenschutzerklärung bleiben. Grau heißt: Cloudflare ist nur Adressbuch, dann kann der Satz raus. Screenshot an Claude genügt. Erledigt sich mit dem Wechsel auf .de, falls .space danach nur noch weiterleitet.
- [ ] **Search Console**: Prüfung „validFrom“ abwarten. Bei Fehler einen Screenshot an Claude.

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
- [ ] Bing Webmaster Tools anlegen (Import aus der Search Console), wichtig für ChatGPT und Copilot.
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
