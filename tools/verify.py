"""Verify static website links and absence of runtime dependencies (stdlib only)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"haftung", "", "apps", "fotostempel", "kaufakte", "vertragsakte", "boxvex", "datenschutz", "datenschutz/fotostempel", "impressum", "kontakt"}
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.headings = [], set(), 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "h1":
            self.headings += 1
        if tag in {"script", "iframe", "form", "embed", "object"}:
            errors.append(f"Unexpected runtime element: {tag}")
        for key in ("href", "src"):
            if key in a:
                self.links.append((tag, key, a[key]))

pages = {}
for name in EXPECTED:
    path = ROOT / name / "index.html"
    if not path.exists():
        errors.append(f"Missing page: {name}")
        continue
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    pages[path.resolve()] = page
    if page.headings != 1:
        errors.append(f"Expected one h1: {name}")
for path, page in pages.items():
    for tag, key, value in page.links:
        url = urlsplit(value)
        if url.scheme or url.netloc:
            if key == "src":
                errors.append(f"External resource: {value}")
            continue
        if value.startswith("/"):
            errors.append(f"Root absolute link breaks project hosting: {value}")
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"Broken link in {path.relative_to(ROOT)}: {value}")
        if url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f"Missing anchor: {value}")
css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
if "@import" in css or "url(" in css:
    errors.append("Unexpected external or unverified CSS resource")
locs = {e.text for e in ET.parse(ROOT / "sitemap.xml").iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
base = "https://stiiblo.github.io/zimmalabs-website/"
if locs != {base + (p + "/" if p else "") for p in EXPECTED}:
    errors.append("Sitemap does not match page inventory")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} pages; links, anchors, sitemap, headings and static dependencies checked.")
