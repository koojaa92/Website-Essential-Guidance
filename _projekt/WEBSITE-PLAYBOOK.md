# Website-Playbook: Websites mit Claude Code bauen

Gelernt aus dem Projekt essential-guidance.space (Herbst 2026). Gedacht als Startdokument für neue Website-Projekte, zum Beispiel für Freundinnen und Freunde mit eigenem Angebot.

**So nutzt du es:** Gib dieses Dokument einem neuen Claude-Code-Chat mit dem Satz: „Lies dieses Playbook. Wir bauen danach eine Website für [Name]. Starte mit Phase 1 und stell mir die Fragen aus dem Interview-Teil.“ Die Vorlagen am Ende (Abschnitt 12) kannst du direkt übernehmen.

---

## 1. Was wesentlich ist (die Haltung)

1. **Erst die Essenz, dann das Design.** Eine Website wird klar, wenn klar ist, wer der Mensch ist, was er anbietet und was er *nicht* anbietet. Das holt man über ein Interview, nicht über Layout-Runden.
2. **Live von Anfang an.** Früh online gehen und dann im echten Browser und auf dem eigenen Handy verfeinern. Feedback am echten Gerät ist zehnmal besser als Feedback an Vorschauen.
3. **Eine Quelle der Wahrheit pro Thema.** Termine stehen in einer Datei, Texte in einem Google Doc, Regeln in `CLAUDE.md`, offene Punkte in `STAND.md`. Nie dieselbe Info an zwei Orten pflegen.
4. **Pragmatisch statt perfekt.** Kleine, schnelle Schritte und sofort live stellen. Was nicht gefällt, wird zurückgedreht. Fast jede Designentscheidung ist umkehrbar.
5. **Die Inhalte gehören dem Menschen.** Claude schreibt Vorschläge, aber Inhaltstexte werden nie ungefragt umgeschrieben. Technik, Abstände und Struktur darf Claude selbstständig verbessern.
6. **Weniger ist mehr.** Wenige Seiten, wenige Schriften, wenige Farben, wenige Tools. Jedes zusätzliche Tool ist ein Konto, ein Login und eine Datenschutzzeile mehr.

---

## 2. Der Werkzeugkasten und wie er zusammenhängt

| Werkzeug | Wofür | Learning |
|---|---|---|
| **Claude (Chat mit Artefakt)** | Erster visueller Entwurf, Look & Feel finden | Gut zum Starten. Für eine echte, wachsende Website zu wenig, dann umziehen. |
| **GitHub** (Repo) | Speichert den Code, jede Änderung als Version | Für kostenloses GitHub Pages muss das Repo **öffentlich** sein. Nichts Geheimes ins Repo legen. |
| **Claude Code (Cloud)** | Baut, prüft (Screenshots) und stellt live | Arbeitet auf einem Entwicklungszweig und schiebt nach `main`. `main` ist live. |
| **GitHub Pages** | Hosting, kostenlos | Live ist der Branch `main`. Ordner mit Unterstrich (`_projekt/`) werden nicht veröffentlicht, ideal für interne Notizen. |
| **Domain** (Cloudflare oder Strato) | Eigene Adresse | **Domain am besten direkt bei Cloudflare kaufen**: Kauf, DNS und Weiterleitungen sind dann an einem Ort. Bei Strato dauert die Freischaltung, und DNS liegt woanders. |
| **Cloudflare DNS** | Domain zeigt auf GitHub Pages | Vier A-Einträge `185.199.108–111.153` plus CNAME `www` → `<user>.github.io`, dazu die Datei `CNAME` im Repo. Mit und ohne www testen. „Cloudflare Pages“ wird **nicht** gebraucht, das hat viel Verwirrung gekostet. |
| **Google Docs** (Connector) | Texte gegenlesen, mit anderen teilen | Claude kann das Doc lesen und schreiben. Gut für Gegenleser ohne Technik. |
| **GoatCounter** | Besucherstatistik ohne Cookies | Kein Cookie-Banner nötig. In der Datenschutzerklärung erwähnen. |
| **Google Search Console / Bing Webmaster** | Gefunden werden | Sitemap einreichen. Bing ist wichtig, weil ChatGPT und Copilot den Bing-Index nutzen. |
| **Eventfrog** (o. Ä.) | Tickets | Website verlinkt pro Termin auf das Ticket. Kein eigenes Bezahlsystem bauen. |
| **Telegram / SoundCloud / Instagram** | Kanäle | Verlinken statt einbetten, wo es geht. Eingebettete Player brauchen einen Datenschutzhinweis. |
| **Newsletter-Tool (Brevo)** | Später | Erst einrichten, wenn wirklich Newsletter verschickt werden. Bis dahin genügt ein Mail-Link „Newsletter-Anmeldung“. |

**Erklärung für Einsteiger (so kurz geben, nicht länger):** GitHub ist der Speicher, GitHub Pages zeigt den Inhalt als Website, die Domain ist das Türschild, Cloudflare leitet das Türschild auf die Website, und Claude Code ist der Handwerker, der im Speicher arbeitet.

**Learning zur Anleitung:** Klickanleitungen für fremde Oberflächen (Cloudflare, Strato, GitHub) immer **Klick für Klick** geben, mit dem genauen Namen des Menüpunkts. Lieber um einen Screenshot bitten als raten. Oberflächen ändern sich, deshalb nie aus dem Gedächtnis beschreiben, ohne es zu sagen.

---

## 3. Der Ablauf in Phasen

**Phase 1: Klären (1 Sitzung)**
- Interview (Abschnitt 4), am besten als Sprachmemo. Transkript an Claude geben.
- Markenarchitektur festlegen: Gibt es eine Dachmarke und mehrere Angebote? Wie heißt was, wie schreibt man es? (Beispiel: „Essenz Raum“ immer zwei Wörter, beide groß.)
- Ergebnis: Seitenliste, Angebotsliste mit Preis, Ort und Zeit, Wörter, die immer und nie vorkommen.

**Phase 2: Entwurf und Live-Gang (1–2 Sitzungen)**
- Statische Seite (HTML, CSS, etwas JS), kein Framework. Ein Repo, GitHub Pages, Domain verbinden.
- Sofort eine `CLAUDE.md` mit den Regeln anlegen (Vorlage in Abschnitt 12).

**Phase 3: Struktur vereinheitlichen**
- Alle Unterseiten nach demselben Muster bauen (Abschnitt 5). Das bringt mehr Ruhe als jede Farbänderung.

**Phase 4: Texte aus dem Interview**
- Claude schreibt aus dem Transkript Texte in der Sprache des Menschen, nicht in Marketingsprache.
- Alt und Neu im Google Doc nebeneinander zeigen. Der Mensch kommentiert, Claude setzt um.

**Phase 5: Design-Feintuning am Gerät**
- Feedback per Handy-Screenshot (Abschnitt 9). Kleine Runden, sofort live.

**Phase 6: Technik, SEO, Recht**
- Strukturierte Daten, Sitemap, `llms.txt`, Search Console, Impressum, Datenschutz (Abschnitte 7, 8, 10).

**Phase 7: Pflege**
- Termine über eine Datei plus Skript. Offene Punkte in `STAND.md`. Gegenleser über das Google Doc.

---

## 4. Interviewfragen (Vorlage)

Ziel: konkret, greifbar und ehrlich. Ruhig konfrontierend fragen. Antworten als Sprachmemo sind ideal, weil sie die echte Sprache des Menschen enthalten.

**Kern**
1. Was machst du, in einem Satz, so dass deine Oma es versteht?
2. Was ist der Kern, der sich durch alle deine Angebote zieht?
3. Wofür willst du *nicht* gehalten werden? (Zum Beispiel: kein Coaching, keine Therapie.)

**Pro Angebot**
4. Was passiert konkret, von der Ankunft bis zum Gehen? Ablauf in Schritten.
5. Für wen ist es, und für wen ausdrücklich nicht?
6. Was nimmt jemand mit, wenn es gut gelaufen ist? Und wenn es „nur“ okay war?
7. Was unterscheidet dich von ähnlichen Angeboten in deiner Stadt? Gibt es eine Lücke (Wochentag, Format, Zielgruppe)?
8. Preis, Ort, Zeit, Anmeldung, Dauer, was ist inklusive?
9. Welche drei Fragen stellen Menschen dir immer wieder? (Wird zur FAQ.)

**Person und Haltung**
10. Was hat dich geprägt (Lehrer, Methoden, Wendepunkte)?
11. Wie hältst du einen Raum? Was tust du, wenn es schwierig wird?
12. Was ist deine Vision, größer als dein Angebot?
13. Ein persönliches Detail, das dich menschlich macht.

**Sprache und Bild**
14. Welche Wörter benutzt du gern, welche magst du gar nicht?
15. Welche Websites findest du schön, welche schrecklich, und warum?
16. Welche Fotos gibt es? Wer ist darauf, und hast du die Rechte?

**Praktisches**
17. Kontaktweg: Mail, Telefon, Messenger? Welche Mailadresse?
18. Ticketing, Newsletter, Social Media: was gibt es schon, was kommt später?
19. Rechtliches: Gewerbe, Umsatzsteuer-Identifikationsnummer, Adresse fürs Impressum.

---

## 5. Struktur, die funktioniert

**Seiten:** Startseite · eine Seite pro Angebot · Über mich · Termine (falls es Termine gibt) · Impressum · Datenschutz.

**Startseite von oben nach unten**
1. **Hero**, der genau einen Bildschirm füllt: Slogan, eine Zeile mit den Angeboten, ein kurzer Absatz, zwei Buttons.
2. **„Was ist [Marke]?“**: ein bis zwei Absätze als Essenz der ganzen Website.
3. **Nächste Termine**, falls vorhanden, automatisch aktuell.
4. **Ein Block pro Angebot**, immer gleich aufgebaut:
   - Goldene Überzeile, die mit der Art beginnt: `Tanz · Sonntags 17–20 Uhr · Ort`
   - Titel, Claim (ein Satz), kurzer Text
   - Zwei Buttons: „Mehr erfahren“ und eine konkrete Handlung
5. **Bleib in Verbindung**: Kanäle (Telegram, Newsletter, SoundCloud), danach der Footer.

**Angebotsseite von oben nach unten**
Hero mit Überzeile · Einstiegstext mit Infobox (Wo, Wann, Preis, Inklusive, Anmeldung) · Ablauf in Schritten · Haltung („Wie ich den Raum halte“) · Was es ausmacht · Termine (nur die nächsten drei) · FAQ · Hinweis (keine Heilkunde).

**Muster, die sich bewährt haben**
- Jede Unterseite hat dieselbe Abfolge. Wer eine kennt, findet sich überall zurecht.
- Die FAQ steht immer auf grauem Hintergrund und am Ende der Seite.
- Preis-Hinweise („Wenn der Preis eine Hürde ist, sprich mich an“) stehen dort, wo die Entscheidung fällt, also unter den Terminen.
- Mail-Buttons mit vorausgefülltem Betreff je nach Button (Anmeldung, Erstgespräch, Newsletter, Booking).

---

## 6. Texte

- **Konkret vor schön.** Erst sagen, was passiert (Ort, Zeit, Ablauf), dann, was es bedeuten kann.
- **Tiefe durch Kürze oder durch Ausführlichkeit, aber bewusst.** Startseite kurz, Unterseiten dürfen ausführlich sein.
- **Eigene Sprache des Menschen** aus dem Interview übernehmen, Marketingfloskeln vermeiden.
- **Feste Schreibweisen** in `CLAUDE.md` festhalten: Markennamen, Ort („immer gleich schreiben“), Mailadresse.
- **Rechtlich heikle Wörter** klären. Beispiel: „Coaching“ nicht als Selbstbezeichnung (Künstlersozialkasse, Abgrenzung), nur verneinend in der FAQ.
- **Fremde Markennamen** nur beschreibend nutzen („inspiriert von Ecstatic Dance“), nie im Titel. Das schützt vor Verwechslung mit anderen Anbietern.
- **Keine einzelnen Wörter am Zeilenende**, Überschriften ausbalancieren (siehe Technik).
- **Satzgröße:** „begegnest“ statt „begegnen kannst“. Kürzer ist in Überschriften fast immer besser.
- **FAQ doppelt pflegen:** sichtbar auf der Seite und als FAQPage-JSON-LD im `<head>`.

---

## 7. Design

**Schrift**
- Zwei Schriften: eine für Überschriften (bei uns Crimson Pro), eine für Fließtext (Karla).
- **Schriften immer in Originalgröße auf der echten Seite vergleichen**, mehrere Varianten nummeriert nebeneinander. Eine Schrift „nach Beschreibung“ auszusuchen ging schief.
- Fonts DSGVO-freundlich laden (Bunny Fonts statt Google Fonts) oder selbst hosten.

**Farben und Flächen**
- Wenige Farben: Dunkelblau, Papierweiß, ein Akzent (Gold). Farben als CSS-Variablen.
- Hintergrundbilder nur dezent, mit Transparenz hinter Farbflächen, nie über Text.
- Graue Flächen markieren Service-Bereiche wie die FAQ.

**Abstände**
- **Eng statt großzügig.** Zu viel Weißraum wirkt leer und zerreißt den Zusammenhang. Eine globale Abstandsregel am Ende der CSS.
- Mehr Abstand zwischen Überschrift und Text als man denkt, weniger zwischen Abschnitten.

**Bilder**
- Ein Bildformat pro Bereich. Kacheln gleich groß und bündig.
- Ähnliche Farbstimmung (leicht entsättigt) wirkt ruhiger als bunte Mischung.
- Personen zum Text hin schauen lassen (Bild bei Bedarf spiegeln).
- **Am Handy wirken Querformate klein.** Quadratisch oder leicht hochkant füllt den Bildschirm besser.
- Terminkarten: Datum groß und leicht transparent ins Bild („4 OKT“), wie auf Flyern.

**Bildschirm-Logik (das wichtigste Design-Learning)**
- **Der Hero füllt genau den ersten Bildschirm**, am Desktop und am Handy. Der nächste Abschnitt erscheint erst beim Scrollen.
- **Am Handy füllt jedes Angebot einen Bildschirm**, mit sanftem Einrasten beim Scrollen. Oben darf das Bild knapp angeschnitten sein, damit spürbar bleibt, dass es weitergeht.
- **Am Desktop ist der Mittelweg richtig:** Das Angebot steht mittig und groß, die Nachbarn schauen schmal herein. Ganz bildschirmfüllend wirkte zu leer und verlor die Reihe der Angebote.
- „Bam, bam, bam, das sind meine Angebote“: Die Abfolge muss als Reihe erkennbar bleiben.

---

## 8. Technik (für Claude Code)

**Grundaufbau**
- Statisches HTML, eine `styles.css`, eine `main.js`. Kein Framework, kein Build-Schritt. So bleibt alles für Claude und Menschen lesbar.
- **Cache:** `styles.css?v=...` und `main.js?v=...` in **allen** HTML-Dateien hochzählen, sonst zeigen Browser die alte Version.
- Neue CSS-Regeln am Ende anhängen und auf **Spezifität** achten. Eine Regel „greift nicht“ meist, weil eine ältere spezifischer ist.

**Handy und iOS Safari**
- `100svh` ist die kleine sichtbare Höhe, `100lvh` die große. Die schwebende Safari-Leiste überlagert den Inhalt, deshalb bei Vollbild-Abschnitten `lvh` und unten etwas Polster.
- Kopfzeilenhöhe per JS messen und als CSS-Variable `--kopf` setzen.
- `scroll-snap-type: y proximity` (sanft), nie `mandatory`.
- `text-wrap: balance` für Überschriften, `pretty` für Text, dazu per JS ein geschütztes Leerzeichen zwischen den letzten zwei Wörtern.

**Prüfen vor jedem Live-Gang**
- Playwright-Screenshots bei **390 px (Handy)** und **1280 px (Desktop)**, bei Layoutfragen auch 1440/1512 px. Chromium liegt im Container unter `/opt/pw-browsers/chromium`.
- Lokal mit `python3 -m http.server` testen. Der Server stirbt manchmal, dann neu starten.
- Screenshots zeigen Fallback-Schriften, wenn Webfonts im Container blockiert sind. Das dem Menschen dazusagen.
- Einblend-Animationen lassen Text im Screenshot blass wirken. Das ist kein Fehler.

**Termine automatisieren**
- Eine Datei `tools/termine.json` (Datum, Art, Ticketlink, Hinweis).
- Ein Skript `tools/make-ics.py` erzeugt daraus die Terminkarten auf allen Seiten, die Kalenderdateien (.ics) und die Event-Daten für Google (JSON-LD mit `validFrom`).
- Karten nie von Hand im HTML ändern.
- Per JS vergangene Termine ausblenden. Der „Nächste Termin“ springt am Abend (bei uns 21 Uhr) weiter.
- Ohne Ticketlink zeigt die Karte „Tickets folgen“.

**Daten für Maschinen**
- JSON-LD: Organisation, Person, Angebot/Service mit Preisen, Events, FAQPage.
- `sitemap.xml`, `robots.txt`, `llms.txt` (Kurzbeschreibung für KI-Systeme, bei Preis- und Zeitänderungen mitpflegen).

**Arbeitsweise im Repo**
- Entwickeln auf einem eigenen Branch, live mit `git push origin <branch>:main`.
- `CLAUDE.md` = verbindliche Regeln. `_projekt/STAND.md` = Stand und To-dos. Beide bei jeder Entscheidung mitpflegen.
- Lange Chats werden irgendwann zusammengefasst. Deshalb gehören wichtige Entscheidungen in diese Dateien, nicht nur in den Chat.

**Google Doc per API pflegen**
- Für Gegenleser: ein Tab „aktuell online“, gegliedert wie die Website (Seite → Abschnitt), goldene Überzeilen, Buttons als `[Button: …]`.
- Technisch: Texte direkt aus dem HTML auslesen, seitenweise einfügen, danach das Doc zurücklesen und die Formatierung anhand der echten Positionen setzen. Grundformat zuerst, Überschriften zuletzt, sonst überschreibt das Grundformat sie.

---

## 9. Feedback geben (was gut funktioniert hat)

**Für den Menschen**
- **Screenshot vom Handy plus ein Satz** („Abstand hier geringer“, „Bild hier größer, 4:5“). Das ist die schnellste und genaueste Form.
- **Ein Punkt pro Nachricht** ist völlig in Ordnung. Viele kleine Nachrichten hintereinander gehen gut.
- **Sprechen statt tippen.** Spracheingabe funktioniert. Claude versteht auch unklare Transkripte und fragt nur nach, wenn es wirklich offen ist.
- Klar sagen, was gemeint ist:
  - „**Nur zeigen**, nicht umsetzen“: Claude macht eine Vorschau als Screenshot.
  - „**Sag erst, was du machen würdest**“: Claude beschreibt Optionen und wartet.
  - „**Mach**“ oder „**umsetzen**“: Claude setzt um, prüft und stellt live.
- Bei Geschmacksfragen den **Mittelweg** anfordern: „Jetzt ist es zu extrem, finde einen Mittelweg.“ Das hat mehrfach zum besten Ergebnis geführt.
- Fremdes Feedback (Freunde, andere KIs) als Text oder Transkript einfügen. Claude ordnet es nach Seiten und setzt es Punkt für Punkt um.

**Für Claude**
- Erst umsetzen, dann kurz berichten. Nicht jede Kleinigkeit erklären.
- Bei größeren Eingriffen (Layout-Umbau, Texte, SEO-Titel) erst Optionen nennen und eine Empfehlung geben.
- Ehrlich sagen, was nicht geprüft werden konnte (zum Beispiel echtes iPhone, echte Schrift).
- Nach jeder Änderung bei 390 und 1280 px prüfen.
- Bei Unklarem in einer Nachricht lieber eine präzise Rückfrage als drei Annahmen.

---

## 10. Recht und Pflichtangaben (Deutschland, keine Rechtsberatung)

- **Impressum:** vollständiger Name, ladungsfähige Anschrift, Kontakt. USt-IdNr. nur, wenn vorhanden. Die normale Steuernummer gehört nicht hinein. Nie Nummern erfinden.
- **Datenschutz:** jedes eingebundene Tool nennen (Hosting, Domain, Statistik, eingebettete Player, Fonts, Ticketing). Am besten Tools wählen, die keinen Cookie-Banner brauchen.
- **Hinweis bei Begleitungsangeboten:** „keine Heilkunde, ersetzt keine Therapie, Teilnahme in Eigenverantwortung“.
- **Affiliate-Links** kennzeichnen.
- **Fotos:** Rechte und Einwilligung der abgebildeten Personen klären, am besten schriftlich.
- **Musikveranstaltungen:** an GEMA denken, sobald öffentlich Tickets verkauft werden.

---

## 11. Was unnötig war (Zeitfresser vermeiden)

- **Zwei Domain-Anbieter.** Domain gleich bei Cloudflare kaufen, dann ist alles an einem Ort.
- **„Cloudflare Pages“ suchen.** GitHub Pages reicht. Cloudflare nur für Domain und DNS.
- **Newsletter-Tool vor dem ersten Newsletter.** Ein Mail-Link genügt am Anfang.
- **Schriftwahl nach Beschreibung.** Immer gleich in Originalgröße vergleichen.
- **Extreme Layout-Lösungen** (komplett bildschirmfüllend, viel Weißraum). Lieber direkt den Mittelweg testen.
- **Alles im Chat lassen.** Entscheidungen in `CLAUDE.md` und `STAND.md` schreiben, sonst gehen sie bei der Zusammenfassung langer Chats verloren.
- **Perfektionismus.** Die Website lebt von den Angeboten. Wenn Struktur, Texte und Handy-Ansicht stimmen, ist sie gut genug.

---

## 12. Vorlagen

### 12.1 Start-Prompt für ein neues Projekt

```
Wir bauen eine Website für [Name], [Beruf/Angebot] in [Stadt].
Lies zuerst das beigefügte Website-Playbook und halte dich an die Haltung und den Ablauf.

Rahmen:
- Statische Website (HTML/CSS/JS), GitHub-Repo [owner/repo], live über GitHub Pages vom Branch main.
- Domain: [domain], DNS bei Cloudflare.
- Sprache: Deutsch, Du-Form.

Arbeitsweise:
- Änderungen sofort umsetzen, bei 390 und 1280 px prüfen, live stellen, kurz berichten.
- Inhaltstexte nie ungefragt umschreiben, nur Vorschläge machen.
- Bei „nur zeigen“ nur eine Vorschau liefern.
- Lege als Erstes CLAUDE.md und _projekt/STAND.md an.

Starte mit Phase 1: Stell mir die Interviewfragen in Blöcken von 4–5 Fragen.
```

### 12.2 CLAUDE.md (Vorlage)

```markdown
# Hinweise für Änderungen an dieser Website

- Live ist der Branch `main` (GitHub Pages).
- Bei Änderungen an styles.css oder main.js die Versionsnummer (?v=...) in allen HTML-Dateien hochzählen.
- Änderungen immer bei 1280 px (Desktop) und 390 px (Handy) prüfen.
- Abstände zwischen Abschnitten eng halten.
- Alle Mail-Links gehen an [mail]. Betreff je nach Button.
- FAQ-Texte zusätzlich als FAQPage-JSON-LD im <head>. Bei Änderungen beides angleichen.
- FAQ-Abschnitte haben grauen Hintergrund.
- Termine nur in tools/termine.json ändern, danach python3 tools/make-ics.py ausführen.
- Projektstand und To-dos: _projekt/STAND.md. Bei neuen Entscheidungen mitpflegen.

## Marke (verbindlich)
- Dachmarke: [Name]. Bereiche: [A], [B], [C].
- Schreibweisen: [...]
- Ort immer gleich: [Ort, Adresse].
- Wörter, die nie vorkommen: [...]
- llms.txt bei Preis-, Zeit- oder Angebotsänderungen mitpflegen.
```

### 12.3 STAND.md (Vorlage)

```markdown
# [Projekt]: Projektstand und offene Punkte
Stand: [Datum]. Live: [URL].

## Was steht
- Marke und Positionierung: ...
- Startseite: ...
- Unterseiten: ...
- Technik und SEO: ...

## Offene Punkte
### Bald
- [ ] ...
### Inhalte
- [ ] ...
### Später
- [ ] ...

## Entschieden (nicht wieder aufmachen)
- ...
```

### 12.4 Nützliche Sätze für Feedback

- „Nur zeigen, nicht umsetzen: Wie sähe es aus, wenn …?“
- „Sag erst, was du machen würdest, bevor du etwas änderst.“
- „Jetzt ist es zu extrem. Finde einen Mittelweg.“
- „Das ist am Handy angeschnitten. Jeder Abschnitt soll auf einen Bildschirm passen.“
- „Schreib alles in die To-do-Liste, ich mache später weiter.“
- „Gleiche das Google Doc mit dem aktuellen Stand der Website ab.“
- „Zeig mir drei Schriften in Originalgröße auf der Seite nebeneinander, nummeriert.“

---

*Die Seite ist lebendig und muss nicht perfekt sein. Sie lebt von den Angeboten.*
