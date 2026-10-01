# Hinweise für Änderungen an dieser Website

- Abstände zwischen den Bereichen (Sections) immer eng halten, nicht großzügig. Globale Regel am Ende von `styles.css`.
- Bei Änderungen an `styles.css` oder `main.js` die Versionsnummer (`?v=...`) in allen HTML-Dateien hochzählen, sonst zeigen Browser die alte Datei.
- Änderungen immer erst am Desktop (1280px) und Handy (390px) prüfen.
- Alle Mail-Links (mailto) gehen an essential-guidance@posteo.de, nicht an hallo@essential-guidance.de.
- FAQ-Texte (details/summary) sind zusätzlich als FAQPage-JSON-LD im <head> hinterlegt; bei FAQ-Änderungen beides angleichen.
- Der Name heißt immer "Essenz Raum" (zwei Wörter, beide groß) in allen sichtbaren Texten. Dateiname essenzraum.html und URLs bleiben unverändert.
- Terminliste ändern: Karten in termine.html/index.html/essential-dance.html/essenzraum.html anpassen, danach 'python3 tools/make-ics.py' ausführen, damit die Kalenderdateien (essential-dance.ics, essenzraum.ics) und die Event-Daten für Google (JSON-LD in termine/essential-dance/essenzraum.html) stimmen.
