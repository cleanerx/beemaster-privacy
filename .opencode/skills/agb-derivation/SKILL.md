---
name: agb-derivation
description: "AGB-/Legal-Ableitung und Veröffentlichung für Beemaster: DE-Master → lokale Fassung, Währung/Preise (EUR/HUF), PAngV/UCPD, Refund, Render- und Web-Sync-Pipeline. Use when: AGB/Rechtstext ändern, neues Land/Währung, HUF-Preise prüfen, legal-render/sync-legal-web, Version/Re-Consent, Legal-Web veröffentlichen."
license: MIT
compatibility: opencode
metadata:
  project: beemaster-privacy
  domain: legal-publishing
  criticality: high
  language: de
---

# AGB-Ableitung (Privacy/Veröffentlichung)

Dieses Repo **publiziert** die aus `beemaster-android` gerenderten Rechtstexte.
Die kanonische Quelle ist Markdown in
`beemaster-android/docs/legal/source/{agb,eula,privacy}/*.md`; die App-HTML ist
eine Ableitung, die Web-HTML in diesem Repo ist eine weitere Ableitung.

## Grundregel: nicht übersetzen, sondern ableiten

Eine lokale AGB ist **keine wörtliche Übersetzung** des DE-Masters. Beim
Ableiten müssen lokale Verbraucher-, Preis- und Währungsregeln berücksichtigt
werden. Insbesondere:

- keine deutschen Rechtsquellen (BGB, PAngV, DDG, BGH) in AT/CH/CZ/HU/PL/…
  stehen lassen, wenn sie dort nicht gelten;
- Preise in **lokaler Währung** und mit dem **konkreten Packpreis**;
- „1 Credit = 5 Cent“ ist **EUR-only**;
- HUF: lokaler Anker **20 HUF/Credit**, Packs 200 / 1.000 / 2.000 / 10.000 HUF;
- keine automatische EUR→HUF-Umrechnung und keine krummen Auto-Werte
  (190/990 HUF) als AGB-Preis übernehmen.

## HUF-Pflichtsatz für die ungarische AGB

> „A kredit árát a Google Play Áruházban megjelenített csomagár határozza meg.
> Az EUR-referenciaár kb. 5 cent; a HUF-csomagár ettől eltérhet.“

Der Satz ist wichtig, weil die AGB sonst „5 cent“ sagt, der ungarische Kunde
aber 20 HUF/Credit zahlt.

## Preis-/Refund-Regeln

1. **PAngV/UCPD:** konkreter Endpreis inkl. USt. in lokaler Währung; kein
   „ca.“-Preis, kein „ab“-Preis als Ersatz für den konkreten Preis.
2. **Pro Credit** nur nennen, wenn es für das konkrete Pack exakt stimmt.
3. **Refund:** in der Kaufwährung.
   - EUR: 5 ct/Credit
   - HUF: 20 HUF/Credit
   - nie pauschal EUR, wenn in HUF gekauft wurde.
4. **Google Play ist Merchant of Record** für Play-Käufe. Die
   Beemaster-Restguthaben-Erstattung ist ein zusätzliches Angebot und ersetzt
   nicht Googles Refund-Prozess.

## Workflow

```bash
# 1. Kanonische Quelle in beemaster-android bearbeiten
#    docs/legal/source/agb/<locale>.md  (NICHT die HTML direkt)

cd ~/dev/git/beemaster-android
python3 scripts/legal-render.py write
python3 scripts/validate-i18n-legal.py
python3 scripts/validate-legal-clauses.py
python3 scripts/validate-legal-versions.py

# 2. Web-Ableitung in beemaster-privacy
python3 scripts/sync-legal-web.py --write
python3 scripts/sync-legal-web.py --check
```

Danach prüfen:

```
[ ] AGB-Version + assets/legal/version.txt konsistent
[ ] Alle Sprachen vorhanden (validate-i18n-legal)
[ ] Pflicht-/Verbotsklauseln je Jurisdiktion (validate-compliance-rules)
[ ] HUF/local-currency-Satz vorhanden
[ ] Keine deutschen Rechtsquellen in fremden Jurisdiktionen
[ ] Web-HTML aus App-HTML abgeleitet (kein manueller Drift)
[ ] Re-Consent/legal_notices geplant, wenn Rechte/Preise betroffen sind
```

## Häufige Fehler

- Web-HTML manuell editieren → wird beim nächsten Sync überschrieben.
- DE-Master wörtlich übersetzen und PAngV/BGB in HU/CZ/PL stehen lassen.
- 5 ct EUR in der HU-AGB lassen, obwohl 20 HUF/Credit gilt.
- Auto-konvertierte 190/990 HUF übernehmen, statt 200/1.000 HUF zu setzen.
- Refund in EUR rechnen, obwohl der Kauf in HUF war.

## Verweise

- `beemaster-business/.opencode/skills/agb-derivation/SKILL.md` (Preise/Währung)
- `beemaster-android/.opencode/skills/legal-compliance-agent/SKILL.md`
- `beemaster-compliance/.opencode/skills/compliance-agent/SKILL.md`
- `catalog/plans.yaml` (kanonische Preise inkl. HUF)
