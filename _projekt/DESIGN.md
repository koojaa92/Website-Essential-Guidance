---
name: Essential Guidance
description: Räume für Bewegung, Präsenz und das, was wesentlich ist.
colors:
  nachtblau: "#14243F"
  nachtblau-weich: "#2A3B57"
  schiefer: "#5A657C"
  gold: "#A87D3A"
  gold-hell: "#C9A76B"
  gold-button: "#BC9455"
  papier: "#FFFFFF"
  nebel: "#F4F6F9"
  linie: "#E3E8F0"
  creme-auf-blau: "#F6F3EC"
typography:
  display:
    fontFamily: "Crimson Pro, Georgia, Times New Roman, serif"
    fontSize: "clamp(2.9rem, 7.6vw, 5.2rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Crimson Pro, Georgia, Times New Roman, serif"
    fontSize: "clamp(2.1rem, 4.6vw, 3.2rem)"
    fontWeight: 700
    lineHeight: 1.08
  title:
    fontFamily: "Crimson Pro, Georgia, Times New Roman, serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.22
  body:
    fontFamily: "Karla, Helvetica Neue, Arial, sans-serif"
    fontSize: "19.5px"
    fontWeight: 400
    lineHeight: 1.68
  label:
    fontFamily: "Karla, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.84rem"
    fontWeight: 600
    letterSpacing: "0.15em"
rounded:
  karte-klein: "8px"
  karte: "14px"
  pille: "999px"
  kreis: "50%"
spacing:
  rand-handy: "1.25rem"
  inhalt-max: "68rem"
  textbreite: "38rem"
components:
  button-primary:
    backgroundColor: "{colors.nachtblau}"
    textColor: "{colors.papier}"
    rounded: "{rounded.pille}"
    padding: "0.82rem 1.6rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.nachtblau}"
    rounded: "{rounded.pille}"
    padding: "0.82rem 1.6rem"
  button-gold:
    backgroundColor: "{colors.gold-button}"
    textColor: "{colors.nachtblau}"
    rounded: "{rounded.pille}"
    padding: "0.82rem 1.6rem"
  karte-auf-blau:
    backgroundColor: "rgba(255,255,255,.05)"
    textColor: "{colors.creme-auf-blau}"
    rounded: "{rounded.karte}"
    padding: "1.6rem"
  infobox:
    backgroundColor: "{colors.papier}"
    textColor: "{colors.nachtblau}"
    rounded: "{rounded.karte-klein}"
    padding: "1.5rem 1.6rem"
---

<!-- Erstellt am 7.10.2026 mit /impeccable document aus dem bestehenden Code (styles.css, HTML-Seiten). Beschreibt den Ist-Zustand; nichts davon ist eine Änderungsvorgabe. Benennungen und North Star sind Vorschläge und können von Jakob angepasst werden. -->

# Design System: Essential Guidance

## Overview

**Creative North Star: "Der gehaltene Raum"** *(Vorschlag; Alternativen: „Nachtblau und Kerzenlicht“, „Ein Schritt nach dem anderen“)*

Die Seite verhält sich wie Jakobs Arbeit: Sie hält Raum, statt zu drängen. Ein tiefes Nachtblau trägt die Abschnitte wie ein abgedunkelter Saal, Gold setzt sparsame Lichtpunkte wie Kerzen auf einem Altar. Fotos aus den echten Räumen (Studio Pro Arte, Altäre, Tanzende, Berge) liefern die Atmosphäre; die Typografie bleibt ruhig und klassisch.

Die Führung ist bewusst langsam: Jeder Abschnitt füllt am Desktop einen Bildschirm, man landet zuerst nur im Bild mit einem Satz und scrollt dann Schritt für Schritt weiter. Texte sind groß genug, dass niemand sich vorbeugen muss. Abstände zwischen Abschnitten sind eng, Weißraum entsteht innerhalb der Abschnitte, nicht zwischen ihnen.

**Key Characteristics:**
- Nachtblau-Gold auf Weiß, mit blauen Bildflächen als Rhythmuswechsel
- Crimson Pro für Stimme und Überschriften, Karla für ruhigen Lesetext
- Goldene Überzeilen in Großbuchstaben als Orientierung (bewusste Entscheidung)
- Ein Bildschirm pro Abschnitt, erster Bildschirm nur Bild und Satz
- Echte Fotos, keine Illustrationen oder Stockmotive

## Colors

Eine zurückhaltende Zwei-Farben-Welt: Nachtblau trägt, Gold leuchtet, Weiß und kühles Nebelgrau geben Luft.

### Primary
- **Nachtblau** (nachtblau): Überschriften, Primär-Buttons, Kopf- und Fußbereich, blaue Abschnittsflächen (Ablauf, Formen der Begleitung, Gene Keys) mit Foto darunter und Blau-Verlauf darüber.

### Secondary
- **Kerzengold** (gold): goldene Überzeilen, Unterstriche der Navigation, Fokus-Rahmen, Akzentlinien unter Überzeilen, Rahmen hervorgehobener Karten.
- **Helles Gold** (gold-hell): Gold auf dunklem Grund (Überzeilen und Zeiten im Ablauf, Termin-Hinweise).
- **Button-Gold** (gold-button): gefüllte Handlungs-Buttons auf Dunkel und auf Terminkarten („Tickets“, „Alle Termine ansehen“ am Handy, Linkseite).

### Neutral
- **Papier** (papier): Grundfläche aller hellen Abschnitte.
- **Nebel** (nebel): FAQ-Abschnitte (immer grau hinterlegt) und Hinweisboxen.
- **Schiefer** (schiefer): Fließtext in zweiter Ebene, Beschriftungen in Infoboxen.
- **Linie** (linie): Rahmen von Infoboxen, Trennlinien, Ghost-Buttons.
- **Creme auf Blau** (creme-auf-blau): Überschriften auf Nachtblau.

### Named Rules
**Die Kerzen-Regel.** Gold ist Licht, nicht Fläche: Überzeilen, feine Linien, Rahmen und wenige gefüllte Handlungs-Buttons. Keine großen Goldflächen.

**Die Ein-Ton-Regel für Blau.** Blaue Abschnitte sind immer Foto plus Nachtblau-Verlauf, nie flaches Blau ohne Bild und nie ein zweiter Blauton.

## Typography

**Display Font:** Crimson Pro (mit Georgia)
**Body Font:** Karla (mit Helvetica Neue, Arial)

**Character:** Eine warme, klassische Buchschrift für Stimme und Haltung, dazu eine klare, freundliche Grotesk für das Lesen. Ernst, aber nicht feierlich.

### Hierarchy
- **Display** (700, clamp(2.9rem, 7.6vw, 5.2rem), 1): Ein Satz pro Seite im Hero, auf Unterseiten zusätzlich durch die Bildschirmhöhe begrenzt.
- **Headline** (700, clamp(2.1rem, 4.6vw, 3.2rem), 1.08): Abschnittsüberschriften.
- **Title** (600, 1.5rem, 1.22): Kartentitel, Ablauf-Schritte, Spaltenüberschriften, FAQ-Fragen.
- **Body** (400, 19.5px Desktop / 19px Handy, 1.68): Fließtext, Textbreite um 38rem. Grundgröße der Seite 17.5px (Handy 17px); in Bildschirm-Abschnitten wächst der Text mit der Bildschirmhöhe.
- **Label** (600, 0.84rem, 0.15em, GROSSBUCHSTABEN): goldene Überzeilen, darunter eine kurze Goldlinie.

### Named Rules
**Die Lesbarkeits-Regel.** Fließtext nie unter 17px und nie in dünner Schrift (Karla 400, nicht 300). Kleingedrucktes nur für Rechtliches und Hinweise.

**Die Überzeilen-Regel.** Überzeilen beginnen mit der Art des Angebots („Tanz ·“, „Workshop ·“, „1:1 ·“) und verbinden Fakten mit Mittelpunkten. Am Handy steht nur der Name.

## Layout

Container bis 68rem (Bildschirm-Abschnitte bis 76–86rem), Seitenrand am Handy 1.25rem. Am Desktop füllt jeder Hauptabschnitt einen Bildschirm (min-height 100vh, Inhalt mittig), ein Bildband plus folgender Abschnitt ergeben zusammen einen Bildschirm. Der Hero jeder Seite füllt den ersten Bildschirm ohne Kopfzeile; am Handy über `lvh`, damit die Safari-Leiste nichts verdeckt. Zweispaltige Raster (Text links, Infobox rechts; Ablauf links, Karten rechts) stapeln sich unter 900–1100px. Angebote auf der Startseite wechseln links/rechts.

**Die Ein-Bildschirm-Regel.** Ein Abschnitt ist ein Gedanke und füllt einen Bildschirm. Nichts darf oben oder unten angeschnitten hineinragen, außer bewusst als Hinweis „es geht weiter“.

**Die Enge-Fugen-Regel.** Zwischen Abschnitten wenig Abstand; Ruhe entsteht im Abschnitt, nicht in weißen Lücken.

## Elevation & Depth

Weitgehend flach. Tiefe entsteht durch Fotos unter Nachtblau-Verläufen und durch halbtransparente Karten auf Blau. Weiche, tiefe Schatten (z. B. `0 20px 40px -28px rgba(15,31,56,.6)`) nur unter Terminkarten und gehobenen Karten.

## Shapes

Weich, aber nicht verspielt: Karten 14px, kleinere Kästen 8px, alle Buttons als Pille (999px), Ablauf-Icons in Kreisen mit goldenem Rand, Bilder mit 8–14px abgerundet.

## Components

### Buttons
- **Shape:** Pille (999px)
- **Primary:** Nachtblau gefüllt, weißer Text (0.82rem 1.6rem); Hover: wird transparent, Text nachtblau. Im Hero: Hover in Gold.
- **Ghost:** transparent mit Linienrahmen, Hover mit Goldrahmen und Goldtext.
- **Gold:** Button-Gold gefüllt mit Nachtblau-Text, für die wichtigste Handlung auf Dunkel oder am Handy.

### Cards / Containers
- **Karten auf Blau:** 14px, `rgba(255,255,255,.05)`, feiner heller oder goldener Rahmen, Titel in Crimson Pro.
- **Infobox (Wo / Wann / Preis):** 8px, Linienrahmen, Begriff links in Schiefer, Wert rechts in Nachtblau, darunter ein breiter Primär-Button.
- **Paketkarten (Einzelbegleitung):** gleich hoch, Details-Button unten auf einer Linie, die aktive Karte bekommt Goldrand und Goldbalken; Details klappen in einen vorbereiteten Raum darunter auf.

### Navigation
- Karla, Schiefer; Hover und aktiv mit Nachtblau und goldenem Unterstrich. Am Handy Menü-Button im Kreis.

### Terminkarten (Signature)
- Foto oben mit großem, halbtransparentem Datum wie auf den Flyern („18 OKT“), darunter Wochentag als goldene Überzeile, Titel, Zeit, Preis und Pillen-Buttons „Tickets“/„Details“. Essenz-Raum-Karten haben einen warmen Cremegrund.

### Ablauf-Schritte (Signature)
- Kreis-Icon mit Goldrand, Uhrzeit darunter, Titel daneben, Text darunter, Trennlinien zwischen den Schritten.

## Do's and Don'ts

### Do:
- **Do** jeden Abschnitt als einen Bildschirm denken und am Desktop (1280px) und Handy (390px) prüfen.
- **Do** echte Fotos aus Jakobs Räumen verwenden, leicht entsättigt und warm.
- **Do** Gold sparsam als Licht einsetzen (Kerzen-Regel).
- **Do** Texte groß und gut lesbar halten (Lesbarkeits-Regel).

### Don't:
- **Don't** bewusste Entscheidungen als „KI-Muster“ zurückbauen: goldene Großbuchstaben-Überzeilen, Mittelpunkte, Crimson Pro + Karla, Blau-Gold.
- **Don't** großzügige weiße Lücken zwischen Abschnitten.
- **Don't** dünne oder kleine graue Fließtexte.
- **Don't** Querformat-Bilder am Handy, wo sie klein wirken; dort lieber quadratisch.
