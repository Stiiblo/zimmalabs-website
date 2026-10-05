# ZimmaLabs Website

Statische Website für FotoStempel, Kaufakte, Vertragsakte und Boxvex. Alle vier Apps sind als **In Vorbereitung** gekennzeichnet. Support: zimmalabs@gmail.com.

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

Im Repository mit Python 3: `python -m http.server 8000` und http://localhost:8000 öffnen. Dieser Server dient ausschließlich der lokalen Vorschau, nicht dem Betrieb.

Automatische Prüfung: `python tools/verify.py`.

## Veröffentlichung erst nach Freigabe

Nach Inhaltsfreigabe und bewusstem Push: GitHub → Settings → Pages → Build and deployment → Deploy from a branch → main → / (root). Kein Actions-Workflow erforderlich. GitHub Free benötigt dafür ein öffentliches Repository. Ohne Custom Domain entsteht die oben genannte kostenlose github.io-Adresse. Hosting-Dokumentation: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Gestaltung und Rechte

Keine fremden Grafiken oder Fontdateien eingebunden. Das FotoStempel-Motiv ist eine CSS-Illustration und ausdrücklich keine echte App-Aufnahme. Keine Behauptung einer pauschalen Rechts- oder Markenfreigabe.
