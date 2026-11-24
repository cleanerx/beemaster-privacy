#!/usr/bin/env python3
"""legal_nav.py — einheitliche Navigation fuer alle Web-Rechts-/Service-Seiten.

Problem: Die Rechtsseiten wurden aus der App-Shell abgeleitet und haben deren
relative Navigation geerbt (`datenschutz.html`, `agb.html`, ...). Auf der
Website existieren diese Dateinamen nicht (`/privacy/datenschutz.html` = 404),
und die Service-Seiten (Kontoloeschung / Datenanfordern) fehlten in der
Navigation der AGB/EULA/Impressum-Seiten ganz.

Dieses Modul baut die Navigation deterministisch neu:

  Datenschutz · AGB · EULA · Impressum · Konto loeschen · Daten anfordern

- Ziele sind die Web-Dateinamen der jeweiligen Locale (mit Fallback auf die
  unsuffigierte Fassung, wenn eine Locale-Datei nicht existiert, z.B. EULA cs).
- Labels: vorhandene (lokalisierte) Labels bleiben erhalten, fehlende kommen
  aus `scripts/service-pages-translations.json`.
- Die eigene Seite wird mit class="active" markiert.

Aufruf:
    python3 scripts/legal_nav.py --check    # exit 1 bei Abweichung
    python3 scripts/legal_nav.py --write
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "scripts" / "service-pages-translations.json"

# Endung -> Inhaltssprache (fuer Labels)
SUFFIX_LANG = {
    "": "de", "_at": "de", "_en": "en", "_cs": "cs", "_fr": "fr",
    "_lu": "fr", "_be": "fr", "_be-nl": "nl", "_nl": "nl", "_pl": "pl",
    "_sk": "sk", "_bg": "bg", "_hu": "hu", "_it": "it", "_da": "da",
}

KINDS = ("privacy", "agb", "eula", "imprint", "del", "req")
STEM_KIND = {"privacy": "privacy", "agb": "agb", "eula": "eula",
             "impressum": "imprint", "konto-loeschen": "del",
             "daten-anfordern": "req"}

NAV_RE = re.compile(r"(?P<indent>[ \t]*)<nav>(?P<body>.*?)</nav>", re.S)
ANCHOR_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', re.S)

# Freigegebene Web-Sprachen (Quelle: beemaster-android/docs/legal/source/
# web_locales.json, "released"). Nur diese erscheinen im Sprachumschalter der
# Rechts-/Service-Seiten; weitere Fassungen werden bewusst nicht angeboten.
RELEASED_SWITCH = (
    ("", "🇩🇪 Deutsch"),
    ("_at", "🇦🇹 Deutsch (AT)"),
    ("_hu", "🇭🇺 Magyar"),
)

SWITCH_RE = re.compile(r'<div class="lang-switch">.*?</div>', re.S)

STEM_BY_KIND = {
    "privacy": "privacy", "agb": "agb", "eula": "eula",
    "imprint": "impressum", "del": "konto-loeschen", "req": "daten-anfordern",
}


def switch_target(kind: str, suffix: str) -> str:
    if kind == "privacy":
        return "index.html" if suffix == "" else f"privacy{suffix}.html"
    return f"{STEM_BY_KIND[kind]}{suffix}.html"


def normalize_lang_switch(html: str, kind: str, suffix: str, indent: str) -> str | None:
    """Beschraenkt den Sprachumschalter auf DE / DE-AT / HU."""
    if not SWITCH_RE.search(html):
        return None
    links = []
    for sfx, label in RELEASED_SWITCH:
        if not (ROOT / switch_target(kind, sfx)).exists():
            continue
        cls = ' class="active"' if sfx == suffix else ""
        links.append(f'<a href="{switch_target(kind, sfx)}"{cls}>{label}</a>')
    block = '<div class="lang-switch">' + (" | ".join(links)) + "</div>"
    return SWITCH_RE.sub(lambda _m: block, html, count=1)


def load_labels() -> dict:
    data = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    return {lang: (entry.get("labels") or {}) for lang, entry in data["languages"].items()}


def parse_name(name: str) -> tuple[str, str] | None:
    stem = name[:-5] if name.endswith(".html") else name
    if stem == "index":
        return "privacy", ""
    for prefix, kind in STEM_KIND.items():
        if stem == prefix:
            return kind, ""
        if stem.startswith(prefix + "_"):
            suffix = stem[len(prefix):]
            if suffix in SUFFIX_LANG:
                return kind, suffix
    return None


def target(kind: str, suffix: str) -> str:
    """Web-Dateiname des Navigationsziels (mit Fallback auf unsuffigiert)."""
    base = {"privacy": "privacy", "agb": "agb", "eula": "eula",
            "imprint": "impressum", "del": "konto-loeschen",
            "req": "daten-anfordern"}[kind]
    if kind == "privacy":
        return "index.html" if suffix == "" else f"privacy{suffix}.html"
    candidate = f"{base}{suffix}.html"
    if suffix and not (ROOT / candidate).exists():
        return f"{base}.html"
    return candidate


def existing_labels(nav_body: str) -> dict[str, str]:
    """Labels der vorhandenen Navigation nach Zielart einsortieren."""
    labels: dict[str, str] = {}
    for href, text in ANCHOR_RE.findall(nav_body):
        name = href.split("/")[-1]
        if name.startswith(("datenschutz", "privacy", "index")):
            kind = "privacy"
        elif name.startswith("konto-loeschen"):
            kind = "del"
        elif name.startswith("daten-anfordern"):
            kind = "req"
        elif name.startswith("agb"):
            kind = "agb"
        elif name.startswith("eula"):
            kind = "eula"
        elif name.startswith("impressum"):
            kind = "imprint"
        else:
            continue
        labels.setdefault(kind, " ".join(text.split()))
    return labels


def nav_block(kind: str, suffix: str, labels: dict, indent: str) -> str:
    lines = ["<nav>"]
    for k in KINDS:
        cls = ' class="active"' if k == kind else ""
        lines.append(f'    <a href="{target(k, suffix)}"{cls}>{labels[k]}</a>')
    lines.append("</nav>")
    return ("\n" + indent).join(lines)


def normalize_html(html: str, name: str, labels_by_lang: dict) -> str | None:
    """Setzt in `html` die einheitliche Navigation (ersetzt oder ergaenzt sie)."""
    parsed = parse_name(name)
    if parsed is None:
        return None
    kind, suffix = parsed

    lang = SUFFIX_LANG[suffix]
    fallback = labels_by_lang.get(lang) or labels_by_lang["de"]
    labels = {k: fallback[k] for k in KINDS}

    match = NAV_RE.search(html)
    if match:
        labels.update(existing_labels(match.group("body")))
        indent = match.group("indent")
        block = nav_block(kind, suffix, labels, indent)
        result = html[:match.start()] + indent + block + html[match.end():]
    else:
        # Seiten ohne Navigation (z.B. die Oesterreich-Fassung) bekommen sie vor <main>.
        main_match = re.search(r"(?P<indent>[ \t]*)<main>", html)
        if not main_match:
            return None
        indent = main_match.group("indent")
        block = nav_block(kind, suffix, labels, indent)
        result = (html[:main_match.start()] + indent + block + "\n\n"
                  + html[main_match.start():])

    switched = normalize_lang_switch(result, kind, suffix, indent)
    return switched or result


def build_nav(name: str, labels_by_lang: dict) -> tuple[str, str] | None:
    html = (ROOT / name).read_text(encoding="utf-8")
    normalized = normalize_html(html, name, labels_by_lang)
    if normalized is None:
        return None
    return normalized, name


def iter_pages() -> list[str]:
    names = []
    for path in sorted(ROOT.glob("*.html")):
        if parse_name(path.name):
            names.append(path.name)
    return names


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not args.write and not args.check:
        ap.error("--write oder --check angeben")

    labels = load_labels()
    changed, total = [], 0
    for name in iter_pages():
        built = build_nav(name, labels)
        if built is None:
            continue
        new_html, _ = built
        total += 1
        current = (ROOT / name).read_text(encoding="utf-8")
        if new_html == current:
            continue
        changed.append(name)
        if args.write:
            (ROOT / name).write_text(new_html, encoding="utf-8")

    if args.check:
        if changed:
            print(f"❌ Navigation driftet: {len(changed)}/{total} Seite(n)")
            for c in changed[:10]:
                print(f"   - {c}")
            return 1
        print(f"OK — Navigation einheitlich ({total} Seiten)")
        return 0

    print(f"Navigation: {len(changed)} von {total} Seite(n) angepasst")
    return 0


if __name__ == "__main__":
    sys.exit(main())
