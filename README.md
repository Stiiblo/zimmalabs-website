# ZimmaLabs Website

Statische Website für FotoStempel, Kaufakte, Vertragsakte und Boxvex. FotoStempel: Android bald verfügbar, iOS geplant. Die übrigen Apps: Android in Vorbereitung, iOS geplant. Keine öffentliche Store-Verfügbarkeit behauptet. Support: zimmalabs@gmail.com.

## Betrieb ohne kostenpflichtige Dienste

Reines HTML und lokales CSS, Systemschriften, kein JavaScript, Backend, Datenbank, Analysewerkzeug, Formular oder extern geladener Inhalt. Keine Paketinstallation und kein Build erforderlich. Kein Kaufprozess. Spätere Store-Links dürfen ausschließlich zum offiziellen Google-Play-Eintrag führen.

Vorgesehen: GitHub Free mit öffentlichem Repository und GitHub Pages, direkt aus dem Branch. Keine Custom Domain und keine CNAME-Datei. Die derzeitigen kostenlosen Bedingungen sind unter [GitHub Pages Quickstart](https://docs.github.com/en/pages/quickstart) dokumentiert; zukünftige Preisänderungen von GitHub können wir nicht garantieren.

Projektadresse: https://stiiblo.github.io/zimmalabs-website/

Relative interne Links funktionieren unter diesem Projekt-Unterpfad. `/apps/` aus der fachlichen Struktur entspricht dort `/zimmalabs-website/apps/`. Alle zehn gewünschten Seiten liegen als Verzeichnisse mit index.html vor.

## Noch keine Veröffentlichung

Das Repository war bei Einrichtung öffentlich, GitHub Pages war noch deaktiviert. GitHub Pages wird durch diesen Auftrag nicht aktiviert. Der Website-Stand soll nach bestandenen Prüfungen auf main gesichert werden. Vor Veröffentlichung fehlen:

Anbieter und Verantwortlicher sind gemäß Nutzerangabe Dario Zimmari, handelnd unter „ZimmaLabs“, Fabrikstrasse 42, 79771 Klettgau, Deutschland. Diese Angaben sind in Impressum und beiden Datenschutzseiten enthalten.

- Die allgemeine Website-/E-Mail-Datenschutzerklärung ist weiterhin ein gesonderter Entwurf. Ihre rechtliche Vervollständigung ist nicht Gegenstand der FotoStempel-App-Erklärung.
- FotoStempel-Datenschutzerklärung: 17 Abschnitte, Stand 5. Oktober 2026, anhand der beiden technischen Audits abgeglichen. Bei einem später veränderten App-Build erneut abgleichen. Keine pauschale rechtliche Konformitätszusage und keine geratenen Rechtsgrundlagen.
- Verifizierte Store-Links erst nach tatsächlicher Veröffentlichung.

Die Website ist noch nicht aktiviert und enthält weiterhin `noindex, nofollow`. Impressum und FotoStempel-Datenschutz enthalten keine Platzhalter oder Entwurfskennzeichnung. Nach Klärung der offenen Punkte diese Kennzeichnungen und Robots-Metadaten bewusst prüfen und entfernen. Die Sitemap ist bereits vorbereitet. Keine Datenschutzerklärungen für die anderen Apps ohne Datenflussprüfung ergänzen.

## Lokal prüfen

Im Repository mit Python 3: `python tools/preview.py` und http://127.0.0.1:8000/zimmalabs-website/ öffnen. Dieser Server dient ausschließlich der lokalen Vorschau, nicht dem Betrieb.

Automatische Prüfung: `python tools/verify.py`.

## Veröffentlichung erst nach Freigabe

Nach Inhaltsfreigabe und bewusstem Push: GitHub → Settings → Pages → Build and deployment → Deploy from a branch → main → / (root). Kein Actions-Workflow erforderlich. GitHub Free benötigt dafür ein öffentliches Repository. Ohne Custom Domain entsteht die oben genannte kostenlose github.io-Adresse. Hosting-Dokumentation: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Gestaltung und Rechte

Eigenes ZL-SVG und reine CSS-Geräteillustration, ausdrücklich keine App-Aufnahme. Original-App-Icons aus den jeweiligen Projekten, Herkunft und Abmessungen in `content/icon-sources.json`. Drei Icons wurden ohne gestalterische Änderungen auf 256 × 256 verkleinert und als verlustfreies WebP gespeichert. Boxvex verwendet eine unveränderte Komposition der tatsächlich referenzierten adaptiven Android-Launcher-Ressourcen; Pfade, Farben und Abstände sind erhalten. Die SVG-Komposition liegt in `content/boxvex-launcher.svg`; das WebP ist 256 × 256 und verlustfrei. Android-Launcher können zusätzlich eine gerätespezifische Außenmaske anwenden. Keine externen Fonts, keine pauschale Marken-/Rechtefreigabe.

## Redesign lokal prüfen

Status und App-Texte zentral in `content/apps.json`. Mit `python tools/build_site.py` die zehn statischen HTML-Seiten neu erzeugen. Python ist nur ein lokales Autorenwerkzeug; GitHub Pages benötigt keinen Build. Rechtstexte liegen unverändert als Inhaltsvorlagen in `content/`. Nach einer Inhaltsänderung generieren und `python tools/verify.py` ausführen.

Design: tiefes Petrol, Champagner, System-Serif für Überschriften und System-Sans für UI. Navigation mobil über natives HTML-details, ganz ohne JavaScript. Lokaler Entwurf zur visuellen Freigabe; kein Commit, Push oder Pages-Wechsel im Redesign-Auftrag.

Prüfung am 5. Oktober 2026: Edge 154.0.4258.53, zehn Seiten × neun Breiten (320, 360, 390, 412, 600, 768, 1024, 1280, 1440 px) × drei Textgrößen (100, 150, 200 Prozent): 270 Layoutprüfungen ohne horizontalen Überlauf oder defekte Bilder. Keine externen Ressourcenrequests und keine Cookies. Mobile Menüsteuerung mit Tastatur und Navigation getestet. Link-/Sitemapprüfung bestanden. Impressum, Datenschutzübersicht, FotoStempel-Datenschutz und Kontakt: Hauptinhalt gegenüber HEAD bytegleich.

Screenshots und Browserprotokoll liegen lokal ignoriert unter `.scratch/redesign-1440.png`, `.scratch/redesign-390.png` und `.scratch/redesign-tests.json`. Boxvex-Icon ergänzt: Manifest → adaptive Launcher-Ressource → Original-Vektor und Hintergrundfarbe eindeutig nachgewiesen. Die bestehende allgemeine Datenschutzübersicht bleibt inhaltlich unverändert, einschließlich ihres bereits vorhandenen Entwurfshinweises.
