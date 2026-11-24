#!/usr/bin/env python3
"""generate-service-pages.py — baut die Service-Seiten (Kontolöschung, Datenanfordern).

Erzeugt fuer ALLE 15 Web-Locales (SUFFIX_MAP wie sync-legal-web.py):
    konto-loeschen{suffix}.html   und   daten-anfordern{suffix}.html

Quellen:
  - scripts/service-pages-translations.json  (Inhalte je Inhaltssprache)
  - Shell der jeweiligen Rechtsseite der Locale (privacy{suffix}.html bzw. index.html)
    → Header (Brand/Subtitle), CSS, Nav, Footer bleiben aus der Shell;
      Titel, Stand-Zeile, Lang-Switch und <main> werden ersetzt.

Hinweise:
  - `sync-legal-web.py` und `restyle` beruehren diese Seiten NICHT (keine Doc-Stems).
  - Sitemap bleibt auf Rechtsdokumente beschraenkt (Service-Seiten sind Play-verlinkt).
  - noindex folgt der Freigabe-Logik der Rechtsseiten (released = de/de-at/hu).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "scripts" / "service-pages-translations.json"
RELEASED_SUFFIXES = {"", "_at", "_hu"}  # docs/legal/source/web_locales.json

sys.path.insert(0, str(Path(__file__).resolve().parent))
from legal_nav import load_labels, normalize_html  # noqa: E402

# locale → (suffix, content-language, label)
LOCALES = [
    ("de", "", "de", "🇩🇪 Deutsch"),
    ("de-at", "_at", "de", "🇦🇹 Deutsch (AT)"),
    ("en", "_en", "en", "🇬🇧 English"),
    ("cs", "_cs", "cs", "🇨🇿 Čeština"),
    ("fr", "_fr", "fr", "🇫🇷 Français"),
    ("lu", "_lu", "fr", "🇱🇺 Luxembourg (FR)"),
    ("be", "_be", "fr", "🇧🇪 Belgique (FR)"),
    ("be-nl", "_be-nl", "nl", "🇧🇪 België (NL)"),
    ("nl", "_nl", "nl", "🇳🇱 Nederlands"),
    ("pl", "_pl", "pl", "🇵🇱 Polski"),
    ("sk", "_sk", "sk", "🇸🇰 Slovenčina"),
    ("bg", "_bg", "bg", "🇧🇬 Български"),
    ("hu", "_hu", "hu", "🇭🇺 Magyar"),
    ("it", "_it", "it", "🇮🇹 Italiano"),
    ("da", "_da", "da", "🇩🇰 Dansk"),
]

SUBTITLES = {
    "del": {
        "de": "Kontolöschung für die Beemaster-App — in der App und außerhalb der App",
        "en": "Account deletion for the Beemaster app — in the app and outside the app",
        "fr": "Suppression du compte pour l'application Beemaster — dans l'application et en dehors",
        "nl": "Accountverwijdering voor de Beemaster-app — in de app en buiten de app",
        "bg": "Изтриване на профила за приложението Beemaster — в приложението и извън него",
        "cs": "Smazání účtu pro aplikaci Beemaster — v aplikaci i mimo ni",
        "da": "Konto-sletning for Beemaster-appen — i appen og uden for appen",
        "hu": "Fióktörlés a Beemaster alkalmazáshoz — az alkalmazásban és kívül",
        "it": "Eliminazione dell'account per l'app Beemaster — nell'app e fuori dall'app",
        "pl": "Usunięcie konta dla aplikacji Beemaster — w aplikacji i poza nią",
        "sk": "Zmazanie účtu pre aplikáciu Beemaster — v aplikácii aj mimo nej",
    },
    "req": {
        "de": "Auskunft und Datenexport für die Beemaster-App (Art. 15 DSGVO)",
        "en": "Access to and export of your data for the Beemaster app (GDPR Art. 15)",
        "fr": "Accès aux données et export pour l'application Beemaster (art. 15 RGPD)",
        "nl": "Inzage en gegevensexport voor de Beemaster-app (art. 15 AVG)",
        "bg": "Достъп и експорт на данни за приложението Beemaster (чл. 15 GDPR)",
        "cs": "Přístup k údajům a export pro aplikaci Beemaster (čl. 15 GDPR)",
        "da": "Indsigt i og eksport af dine data for Beemaster-appen (GDPR art. 15)",
        "hu": "Hozzáférés az adataihoz azok exportálásához (GDPR 15. cikk)",
        "it": "Accesso ed esportazione dei dati per l'app Beemaster (art. 15 GDPR)",
        "pl": "Dostęp do danych i ich eksport dla aplikacji Beemaster (art. 15 RODO)",
        "sk": "Prístup k údajom a ich export pre aplikáciu Beemaster (čl. 15 GDPR)",
    },
}

PAGES = ("del", "req")


def legal_shell(locale: str, suffix: str) -> str:
    """Shell aus der Rechtsseite der Locale (privacy{suffix}.html / index.html)."""
    name = "index.html" if suffix == "" else f"privacy{suffix}.html"
    path = ROOT / name
    if not path.exists():
        raise SystemExit(f"❌ Shell fehlt: {name}")
    return path.read_text(encoding="utf-8")


# Freigegebene Web-Sprachen (web_locales.json "released"): nur DE/AT/HU.
RELEASED_SWITCH = (("", "🇩🇪 Deutsch"), ("_at", "🇦🇹 Deutsch (AT)"), ("_hu", "🇭🇺 Magyar"))


def lang_switch(page_stem: str, suffix: str) -> str:
    parts = []
    for sfx, label in RELEASED_SWITCH:
        cls = ' class="active"' if sfx == suffix else ""
        parts.append(f'<a href="{page_stem}{sfx}.html"{cls}>{label}</a>')
    return '<div class="lang-switch">' + " | ".join(parts) + "</div>"


def build_main(t: dict, lang: str, page: str, suffix: str) -> str:
    p = t[page]
    out = [f"<main>\n<h1>{p['title']}</h1>",
           f'<p class="subtitle">{SUBTITLES[page][lang]}</p>']
    if t.get("provider"):
        out.append(f'<p class="provider">{t["provider"]}</p>')
    out.append(f"<p>{p['intro']}</p>")
    out.append(f"<h2>{p['s1_h']}</h2>")
    out.append("<ul>\n" + "\n".join(f"<li>{li}</li>" for li in p["s1_li"]) + "\n</ul>")
    out.append(f"<h2>{p['s2_h']}</h2>")
    out.append(f"<p>{p['s2_p']}</p>")
    out.append("<ul>\n" + "\n".join(f"<li>{li}</li>" for li in p["s2_li"]) + "\n</ul>")
    out.append(f"<h2>{p['s3_h']}</h2>")
    out.append('<table class="data-table">')
    out.append("<tr>" + "".join(f"<th>{c}</th>" for c in p["s3_head"]) + "</tr>")
    for row in p["s3_rows"]:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
    out.append("</table>")
    if "s4_h" in p:
        out.append(f"<h2>{p['s4_h']}</h2>")
        out.append("<ul>\n" + "\n".join(f"<li>{li}</li>" for li in p["s4_li"]) + "\n</ul>")

    # Cross-Links (sibling service page + Rechtsdokumente der Locale)
    labels = t["labels"]
    privacy_href = "index.html" if suffix == "" else f"privacy{suffix}.html"
    links = [
        f'<a href="{("konto-loeschen" if page == "req" else "daten-anfordern")}{suffix}.html">{labels["del"] if page == "req" else labels["req"]}</a>',
        f'<a href="{privacy_href}">{labels["privacy"]}</a>',
        f'<a href="agb{suffix}.html">{labels["agb"]}</a>',
        f'<a href="eula{suffix}.html">{labels["eula"]}</a>',
        f'<a href="impressum{suffix}.html">{labels["imprint"]}</a>',
    ]
    out.append("<p>" + " · ".join(links) + "</p>")
    out.append("</main>")
    return "\n".join(out)


def build_page(locale: str, suffix: str, content_lang: str, languages: dict,
               page: str, stem: str) -> tuple[str, str]:
    shell = legal_shell(locale, suffix)
    p = languages[content_lang][page]

    shell = re.sub(r"<title>.*?</title>",
                   f"<title>{p['title']} | Beemaster</title>", shell, count=1, flags=re.S)
    shell = re.sub(r'(<p class="last-updated">).*?(</p>)',
                   lambda m: f"{m.group(1)}{p['updated']}{m.group(2)}", shell, count=1, flags=re.S)
    shell = re.sub(r'(<p class="subtitle">).*?(</p>)',
                   lambda m: f"{m.group(1)}{SUBTITLES[page][content_lang]}{m.group(2)}",
                   shell, count=1, flags=re.S)
    shell = re.sub(r'<div class="lang-switch">.*?</div>',
                   lambda _m: lang_switch(stem, suffix), shell, count=1, flags=re.S)

    m_start = shell.find("<main>")
    m_end = shell.find("</main>")
    if m_start < 0 or m_end < 0:
        raise SystemExit(f"❌ <main> nicht gefunden in Shell der Locale {locale}")
    shell_pre = shell[:m_start]
    shell_post = shell[m_end:]

    html = shell_pre + "\n" + build_main(languages[content_lang], content_lang, page, suffix) + "\n" + shell_post
    target = f"{stem}{suffix}.html"
    normalized = normalize_html(html, target, load_labels())
    return target, (normalized or html)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Seiten erzeugen/überschreiben")
    parser.add_argument("--check", action="store_true", help="nur Differenz zeigen")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("--write oder --check angeben")

    t = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    languages = t.get("languages") or {}
    missing = [lang for _loc, _sfx, lang, _label in LOCALES if lang not in languages]
    if missing:
        raise SystemExit(f"❌ Übersetzungen fehlen für: {', '.join(sorted(set(missing)))}")

    changed, unchanged, skipped = [], [], []
    for locale, suffix, content_lang, _label in LOCALES:
        for page in PAGES:
            stem = "konto-loeschen" if page == "del" else "daten-anfordern"
            target, html = build_page(locale, suffix, content_lang, languages, page, stem)
            path = ROOT / target
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current == html:
                unchanged.append(target)
                continue
            if args.check:
                changed.append(target)
                continue
            path.write_text(html, encoding="utf-8")
            changed.append(target)
            print(f"WRITTEN: {target}")

    if args.check:
        if changed:
            print(f"❌ Drift: {len(changed)} Datei(en) — generate-service-pages.py --write")
            for c in changed:
                print(f"   - {c}")
            return 1
        print("OK — alle Service-Seiten konsistent")
        return 0

    print(f"Service-Seiten: {len(changed)} geschrieben, {len(unchanged)} unverändert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
