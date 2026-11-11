# Requirements — beemaster-privacy

> **Generiert** aus `requirements/requirements.json`. Nicht von Hand editieren.  
> Kanonischer Katalog: `beemaster-compliance/rules/legal-rules.json` (Version 2026-10-09).  
> Konvention: `beemaster-process/docs/requirements-convention.md`.  
> Generator: `python3 scripts/generate-requirements.py`.

Rechtstext-Veröffentlichung (AGB/EULA/Privacy/Impressum) und Render-Pipeline.

## Übersicht

**implemented**: 5

| ID | Art | Status | Titel |
|---|---|---|---|
| `DSGVO-ART13-PRIVACY-INFO` | legal | implemented | Datenschutzinformation |
| `DSGVO-ART13-PRIVACY-WEB` | legal | implemented | Datenschutzinformation im Web |
| `EU-CRD-ART9-WITHDRAWAL` | legal | implemented | Widerrufsrecht im Rechtstext |
| `BILL-MOR-PLAY-MIRROR` | legal | implemented | Google Play als Merchant of Record im Rechtstext |
| `DE-DDG-5-IMPRINT-WEB` | legal | implemented | Impressum im Web |

## DSGVO-ART13-PRIVACY-INFO — Datenschutzinformation

- **Art:** `legal`
- **Status:** `implemented`
- **Owner:** legal

**Checks/Gates:** `privacy-legal-render`, `privacy-legal-review-hints`

**Doku:** `privacy_en.html`

## DSGVO-ART13-PRIVACY-WEB — Datenschutzinformation im Web

- **Art:** `legal`
- **Status:** `implemented`
- **Owner:** legal

**Checks/Gates:** `privacy-legal-render`

**Doku:** `privacy_en.html`

## EU-CRD-ART9-WITHDRAWAL — Widerrufsrecht im Rechtstext

- **Art:** `legal`
- **Status:** `implemented`
- **Owner:** legal

**Checks/Gates:** `privacy-legal-render`

**Doku:** `agb.html`

## BILL-MOR-PLAY-MIRROR — Google Play als Merchant of Record im Rechtstext

- **Art:** `legal`
- **Status:** `implemented`
- **Owner:** legal

**Checks/Gates:** `privacy-legal-render`

**Doku:** `agb.html`

## DE-DDG-5-IMPRINT-WEB — Impressum im Web

- **Art:** `legal`
- **Status:** `implemented`
- **Owner:** legal

**Checks/Gates:** `privacy-legal-render`

**Doku:** `impressum.html`
