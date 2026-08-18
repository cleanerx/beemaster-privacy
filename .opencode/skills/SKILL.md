---
name: legal-compliance-agent
description: Maschinenlesbares Compliance-Regelwerk für Beemaster Android Legal-Dokumente (DE, AT, CZ, EU). Prüft AGB, EULA, Datenschutz, Impressum auf Vollständigkeit und Rechtskonformität.
compatibility: opencode
---

# Legal Compliance Agent Skill

**Name:** legal-compliance-agent  
**Beschreibung:** Maschinenlesbares Compliance-Regelwerk für Beemaster Android Legal-Dokumente (Deutschland, Österreich, Tschechien, EU). Prüft AGB, EULA, Datenschutzerklärung, Impressum auf Vollständigkeit und Rechtskonformität.

---

## 📋 Überblick

Dieser Skill bietet:
- Maschinenlesbare Compliance-Regeln (JSON) für alle Rechtsräume (DE, AT, CZ, EU)
- Reproduzierbare Validierungsskripte
- Referenzen auf Gesetzestexte und Behörden
- Automatisierte Prüfung vor jedem Release

---

## 🏛️ Maschinenlesbare Compliance-Regeln (JSON)

**Datei:** `docs/COMPLIANCE/legal-rules.json`

```json
{
  "version": "2026-08-18",
  "lastUpdated": "2026-08-18T00:00:00Z",
  "jurisdictions": {
    "DE": {
      "name": "Deutschland",
      "language": "de",
      "assetFolder": "legal/de",
      "laws": [
        {
          "id": "DE-DSGVO",
          "name": "DSGVO",
          "fullName": "Datenschutz-Grundverordnung",
          "url": "https://dsgvo-gesetz.de/",
          "type": "EU-Verordnung (direkt anwendbar)",
          "requirements": [
            "Art. 5: Grundsätze der Verarbeitung",
            "Art. 6: Rechtsgrundlagen",
            "Art. 7: Bedingungen für die Einwilligung",
            "Art. 12-14: Informationspflichten",
            "Art. 15-22: Betroffenenrechte",
            "Art. 77: Beschwerderecht"
          ]
        },
        {
          "id": "DE-BDSG",
          "name": "BDSG",
          "fullName": "Bundesdatenschutzgesetz",
          "url": "https://www.gesetze-im-internet.de/bdsg_2018/",
          "type": "Nationales Recht",
          "requirements": [
            "§1: Zweck des Gesetzes",
            "§26: Beschäftigtendatenschutz"
          ]
        },
        {
          "id": "DE-DDG",
          "name": "DDG",
          "fullName": "Digitale-Dienste-Gesetz",
          "url": "https://www.gesetze-im-internet.de/ddg/",
          "type": "Nationales Recht",
          "requirements": [
            "§5: Impressumspflicht"
          ]
        },
        {
          "id": "DE-VSBG",
          "name": "VSBG",
          "fullName": "Verbraucherstreitbeilegungsgesetz",
          "url": "https://www.gesetze-im-internet.de/vsb/",
          "type": "Nationales Recht",
          "requirements": [
            "§36: Information über außergerichtliche Streitbeilegung"
          ]
        },
        {
          "id": "DE-BGB",
          "name": "BGB",
          "fullName": "Bürgerliches Gesetzbuch",
          "url": "https://www.gesetze-im-internet.de/bgb/",
          "type": "Nationales Recht",
          "requirements": [
            "§§312 ff.: Widerrufsrecht bei Fernabsatzverträgen",
            "§§327 ff.: Verträge über digitale Produkte",
            "§195: Verjährungsfrist (3 Jahre)"
          ]
        }
      ],
      "supervisoryAuthority": {
        "name": "Der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Baden-Württemberg",
        "address": "Lautenschlagerstraße 20, 70173 Stuttgart",
        "email": "poststelle@lfdi.bwl.de",
        "url": "https://www.baden-wuerttemberg.datenschutz.de"
      },
      "disputeResolution": {
        "name": "Verbraucherschlichtungsstelle (nicht teilnahmebereit)",
        "url": "https://www.verbraucherstreitbeilegung-zentrum.de/"
      },
      "mandatoryClauses": {
        "impressum": ["§5 DDG", "Kontaktangaben", "Haftungsausschluss"],
        "privacy": ["DSGVO Art. 13", "Betroffenenrechte", "Aufsichtsbehörde DE"],
        "agb": ["§36 VSBG", "Widerrufsbelehrung", "Gerichtsstand"],
        "eula": ["Gewährleistung", "Haftung", "Rechtswahl DE"]
      },
      "forbiddenClauses": {
        "impressum": ["VSBG-Link (EU-ODR aufgehoben)"],
        "privacy": ["Keine"],
        "agb": ["AStG (gilt nur für AT)"],
        "eula": ["ABGB (gilt nur für AT)"]
      }
    },
    "AT": {
      "name": "Österreich",
      "language": "de-at",
      "assetFolder": "legal/de-at",
      "laws": [
        {
          "id": "AT-DSGVO",
          "name": "DSGVO",
          "fullName": "Datenschutz-Grundverordnung",
          "url": "https://gdpr-info.eu/",
          "type": "EU-Verordnung (direkt anwendbar)",
          "requirements": [
            "Art. 5: Grundsätze der Verarbeitung",
            "Art. 6: Rechtsgrundlagen",
            "Art. 7: Bedingungen für die Einwilligung",
            "Art. 12-14: Informationspflichten",
            "Art. 15-22: Betroffenenrechte",
            "Art. 77: Beschwerderecht"
          ]
        },
        {
          "id": "AT-DSG",
          "name": "DSG",
          "fullName": "Datenschutzgesetz 2000",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001222",
          "type": "Nationales Recht",
          "requirements": [
            "§1: Grundsätze",
            "§4: Einwilligungsfähigkeit (14 Jahre)",
            "§24: Beschwerderecht bei DSB"
          ]
        },
        {
          "id": "AT-ECG",
          "name": "ECG",
          "fullName": "E-Commerce-Gesetz",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20000644",
          "type": "Nationales Recht",
          "requirements": [
            "§5: Anbieterkennzeichnung"
          ]
        },
        {
          "id": "AT-MedienG",
          "name": "MedienG",
          "fullName": "Mediengesetz",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10000682",
          "type": "Nationales Recht",
          "requirements": [
            "§24: Offenlegungspflicht",
            "§25: Medieninhaber"
          ]
        },
        {
          "id": "AT-FAGG",
          "name": "FAGG",
          "fullName": "Fern- und Auswärtsgeschäfte-Gesetz",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009247",
          "type": "Nationales Recht",
          "requirements": [
            "§11: Rücktrittsrecht (14 Tage)",
            "§13a: Widerrufsbutton (ab 1.10.2026)",
            "§18: Ausnahmen bei digitalen Inhalten"
          ]
        },
        {
          "id": "AT-KSchG",
          "name": "KSchG",
          "fullName": "Konsumentenschutzgesetz",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10000689",
          "type": "Nationales Recht",
          "requirements": [
            "§1: Geltungsbereich",
            "§14: Unzulässige Gerichtsstandsvereinbarungen"
          ]
        },
        {
          "id": "AT-AStG",
          "name": "AStG",
          "fullName": "Alternativ-Streitbeilegung-Gesetz",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009248",
          "type": "Nationales Recht",
          "requirements": [
            "§19: Information über Schlichtungsstellen"
          ],
          "note": "Gilt nur für in Österreich niedergelassene Unternehmer"
        },
        {
          "id": "AT-ABGB",
          "name": "ABGB",
          "fullName": "Allgemeines Bürgerliches Gesetzbuch",
          "url": "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10000528",
          "type": "Nationales Recht",
          "requirements": [
            "§932: Gewährleistung",
            "§14: Verjährung"
          ]
        }
      ],
      "supervisoryAuthority": {
        "name": "Datenschutzbehörde (DSB)",
        "address": "Barichgasse 40-42, 1030 Wien",
        "email": "dsb@dsb.gv.at",
        "url": "https://www.dsb.gv.at"
      },
      "disputeResolution": [
        {
          "name": "Internet Ombudsstelle (ÖIAT)",
          "address": "Mariahilfer Straße 103/1/18, 1060 Wien",
          "email": "office@ombudsstelle.at",
          "url": "https://www.ombudsstelle.at"
        },
        {
          "name": "Schlichtung für Verbrauchergeschäfte",
          "address": "Mariahilfer Straße 103/1/18, 1060 Wien",
          "email": "office@schlichtung.at",
          "url": "https://www.schlichtung.at"
        }
      ],
      "mandatoryClauses": {
        "impressum": ["§5 ECG", "§24 MedienG", "Medieninhaber", "Bruttopreise"],
        "privacy": ["DSGVO Art. 13", "DSG §24", "Beschwerderecht DSB"],
        "agb": ["§1 KSchG", "§11 FAGG (Rücktritt)", "§19 AStG (Schlichtung)", "§14 KSchG (Gerichtsstand)"],
        "eula": ["ABGB §932 (Gewährleistung)", "KSchG", "Rechtswahl AT"]
      },
      "forbiddenClauses": {
        "impressum": ["VSBG-Link", "COI-Link (tschechisch)"],
        "privacy": ["BDSG (nur DE)", "BfDI (nur DE)"],
        "agb": ["VSBG (nur DE)", "BGB (nur DE)"],
        "eula": ["BGB (nur DE)"]
      }
    },
    "CZ": {
      "name": "Tschechien",
      "language": "cs",
      "assetFolder": "legal/cs",
      "laws": [
        {
          "id": "CZ-GDPR",
          "name": "GDPR",
          "fullName": "General Data Protection Regulation",
          "url": "https://gdpr.eu/",
          "type": "EU-Verordnung (direkt anwendbar)",
          "requirements": [
            "Art. 5: Grundsätze der Verarbeitung",
            "Art. 6: Rechtsgrundlagen",
            "Art. 7: Bedingungen für die Einwilligung",
            "Art. 12-14: Informationspflichten",
            "Art. 15-22: Betroffenenrechte",
            "Art. 77: Beschwerderecht"
          ]
        },
        {
          "id": "CZ-110/2019",
          "name": "Zákon č. 110/2019 Sb.",
          "fullName": "Gesetz über die Verarbeitung personenbezogener Daten",
          "url": "https://www.uoou.cz/",
          "type": "Nationales Recht",
          "requirements": [
            "§7: Einwilligungsfähigkeit (15 Jahre)",
            "§24: Beschwerde bei ÚOOÚ"
          ]
        },
        {
          "id": "CZ-89/2012",
          "name": "Zákon č. 89/2012 Sb.",
          "fullName": "Občanský zákoník (Bürgerliches Gesetzbuch)",
          "url": "https://www.zakonyprolidi.cz/cs/2012-89",
          "type": "Nationales Recht",
          "requirements": [
            "§1811: Informationspflichten",
            "§1829: Widerrufsrecht (14 Tage)"
          ]
        },
        {
          "id": "CZ-634/1992",
          "name": "Zákon č. 634/1992 Sb.",
          "fullName": "Gesetz über den Verbraucherschutz",
          "url": "https://www.zakonyprolidi.cz/cs/1992-634",
          "type": "Nationales Recht",
          "requirements": [
            "§14: Außergerichtliche Streitbeilegung"
          ]
        }
      ],
      "supervisoryAuthority": {
        "name": "ÚOOÚ (Úřad pro ochranu osobních údajů)",
        "address": "Pplk. Sochora 27, 170 00 Praha 7",
        "email": "posta@uoou.gov.cz",
        "url": "https://www.uoou.cz/"
      },
      "disputeResolution": {
        "name": "Česká obchodní inspekce (COI)",
        "address": "Ústřední inspektorát – oddělení ADR, Gorazdova 1969/24, 120 00 Praha 2",
        "email": "adr@coi.gov.cz",
        "url": "https://coi.gov.cz/informace-o-adr/"
      },
      "mandatoryClauses": {
        "impressum": ["§5 DDG (DE-Anbieter)", "Kontaktangaben"],
        "privacy": ["GDPR Art. 13", "Zákon 110/2019 Sb.", "Beschwerderecht ÚOOÚ"],
        "agb": ["§14 Zákon 634/1992 Sb. (ADR)", "Widerrufsbelehrung"],
        "eula": ["Gewährleistung", "Rechtswahl mit Art. 6 Rom-I"]
      },
      "forbiddenClauses": {
        "impressum": ["VSBG-Link"],
        "privacy": ["BDSG (nur DE)"],
        "agb": ["VSBG (nur DE)", "AStG (nur AT)"],
        "eula": ["BGB (nur DE)", "ABGB (nur AT)"]
      }
    },
    "EU": {
      "name": "Europäische Union",
      "language": "en",
      "assetFolder": "legal/en",
      "laws": [
        {
          "id": "EU-GDPR",
          "name": "GDPR",
          "fullName": "General Data Protection Regulation (EU) 2016/679",
          "url": "https://gdpr-info.eu/",
          "type": "EU-Verordnung",
          "requirements": [
            "Art. 5: Principles of processing",
            "Art. 6: Lawfulness of processing",
            "Art. 7: Conditions for consent",
            "Art. 12-14: Transparency obligations",
            "Art. 15-22: Data subject rights",
            "Art. 77: Right to lodge a complaint"
          ]
        },
        {
          "id": "EU-2011/83",
          "name": "Consumer Rights Directive",
          "fullName": "Directive 2011/83/EU",
          "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011L0083",
          "type": "EU-Richtlinie",
          "requirements": [
            "Art. 6: Information requirements",
            "Art. 9: Right of withdrawal (14 days)",
            "Art. 14: Effects of withdrawal"
          ]
        },
        {
          "id": "EU-2019/770",
          "name": "Digital Content Directive",
          "fullName": "Directive (EU) 2019/770",
          "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0770",
          "type": "EU-Richtlinie",
          "requirements": [
            "Conformity of digital content",
            "Remedies for lack of conformity"
          ]
        }
      ],
      "supervisoryAuthority": {
        "name": "EDPB (European Data Protection Board)",
        "url": "https://www.edpb.europa.eu/"
      },
      "disputeResolution": {
        "name": "EU Consumer Redress",
        "url": "https://consumer-redress.ec.europa.eu/dispute-resolution-bodies"
      },
      "mandatoryClauses": {
        "impressum": ["Contact information", "Liability disclaimer"],
        "privacy": ["GDPR Art. 13", "Data subject rights", "Supervisory authority"],
        "agb": ["Withdrawal policy", "Dispute resolution info"],
        "eula": ["Warranty", "Liability", "Governing law"]
      },
      "forbiddenClauses": {
        "impressum": ["EU ODR platform (abolished 2025-07-20)"],
        "privacy": ["None"],
        "agb": ["None"],
        "eula": ["None"]
      }
    }
  },
  "validationRules": [
    {
      "id": "RULE-001",
      "name": "Impressum Contact Info",
      "description": "All jurisdictions require valid contact information in imprint",
      "appliesTo": ["DE", "AT", "CZ", "EU"],
      "document": "impressum",
      "check": "contains",
      "patterns": ["E-Mail", "Anschrift", "Adresse"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-002",
      "name": "Privacy GDPR Art. 13",
      "description": "Privacy policy must reference GDPR Art. 13 information requirements",
      "appliesTo": ["DE", "AT", "CZ", "EU"],
      "document": "privacy",
      "check": "contains",
      "patterns": ["Art. 13", "Art 13", "Article 13"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-003",
      "name": "Privacy Supervisory Authority",
      "description": "Privacy policy must name the competent supervisory authority",
      "appliesTo": ["DE", "AT", "CZ", "EU"],
      "document": "privacy",
      "check": "contains",
      "patterns": ["Aufsichtsbehörde", "Supervisory authority", "Datenschutzbehörde"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-004-DE",
      "name": "DE Impressum §5 DDG",
      "description": "German imprint must reference §5 DDG/TMG",
      "appliesTo": ["DE"],
      "document": "impressum",
      "check": "contains",
      "patterns": ["§5 DDG", "§5 TMG"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-005-DE",
      "name": "DE AGB §36 VSBG",
      "description": "German AGB must reference §36 VSBG dispute resolution",
      "appliesTo": ["DE"],
      "document": "agb",
      "check": "contains",
      "patterns": ["§36 VSBG", "VSBG"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-006-AT",
      "name": "AT Impressum §5 ECG",
      "description": "Austrian imprint must reference §5 ECG",
      "appliesTo": ["AT"],
      "document": "impressum",
      "check": "contains",
      "patterns": ["§5 ECG", "E-Commerce-Gesetz"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-007-AT",
      "name": "AT AGB FAGG Rücktritt",
      "description": "Austrian AGB must include FAGG withdrawal policy",
      "appliesTo": ["AT"],
      "document": "agb",
      "check": "contains",
      "patterns": ["§11 FAGG", "Rücktrittsrecht", "Rücktritt"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-008-AT",
      "name": "AT AGB AStG Schlichtung",
      "description": "Austrian AGB must reference AStG dispute resolution",
      "appliesTo": ["AT"],
      "document": "agb",
      "check": "contains",
      "patterns": ["§19 AStG", "AStG", "Schlichtung"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-009-AT",
      "name": "AT Privacy DSB",
      "description": "Austrian privacy must name Datenschutzbehörde (DSB)",
      "appliesTo": ["AT"],
      "document": "privacy",
      "check": "contains",
      "patterns": ["Datenschutzbehörde", "DSB", "Barichgasse"],
      "severity": "ERROR"
    },
    {
      "RULE-010-AT": "RULE-010-AT",
      "name": "AT EULA ABGB",
      "description": "Austrian EULA must reference ABGB governing law",
      "appliesTo": ["AT"],
      "document": "eula",
      "check": "contains",
      "patterns": ["ABGB", "österreichisches Recht", "Allgemeines Bürgerliches Gesetzbuch"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-011-CZ",
      "name": "CZ Privacy ÚOOÚ",
      "description": "Czech privacy must name ÚOOÚ supervisory authority",
      "appliesTo": ["CZ"],
      "document": "privacy",
      "check": "contains",
      "patterns": ["ÚOOÚ", "Úřad pro ochranu osobních údajů"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-012-CZ",
      "name": "CZ AGB COI ADR",
      "description": "Czech AGB must reference COI dispute resolution",
      "appliesTo": ["CZ"],
      "document": "agb",
      "check": "contains",
      "patterns": ["Česká obchodní inspekce", "COI", "adr@coi.gov.cz"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-013-EU",
      "name": "EU No ODR Platform",
      "description": "EU documents must not reference abolished EU ODR platform (abolished 2025-07-20)",
      "appliesTo": ["DE", "AT", "CZ", "EU"],
      "document": "all",
      "check": "notContains",
      "patterns": ["ec.europa.eu/odr", "Online-Streitbeilegungs-Plattform"],
      "severity": "WARNING"
    },
    {
      "id": "RULE-014-DE",
      "name": "DE No AStG",
      "description": "German documents must not reference Austrian AStG",
      "appliesTo": ["DE"],
      "document": "all",
      "check": "notContains",
      "patterns": ["AStG", "Alternativ-Streitbeilegung-Gesetz (Österreich)"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-015-DE",
      "name": "DE No ABGB",
      "description": "German documents must not reference Austrian ABGB",
      "appliesTo": ["DE"],
      "document": "all",
      "check": "notContains",
      "patterns": ["ABGB", "Allgemeines Bürgerliches Gesetzbuch (Österreich)"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-016-AT",
      "name": "AT No VSBG",
      "description": "Austrian documents must not reference German VSBG",
      "appliesTo": ["AT"],
      "document": "all",
      "check": "notContains",
      "patterns": ["VSBG", "Verbraucherstreitbeilegungsgesetz (Deutschland)"],
      "severity": "ERROR"
    },
    {
      "id": "RULE-017-AT",
      "name": "AT No BGB",
      "description": "Austrian documents must not reference German BGB",
      "appliesTo": ["AT"],
      "document": "all",
      "check": "notContains",
      "patterns": ["BGB", "Bürgerliches Gesetzbuch (Deutschland)"],
      "severity": "ERROR"
    }
  ],
  "reConsentRules": {
    "required": [
      "Neue Datenkategorien",
      "Neue Verarbeitungszwecke",
      "Neue Drittanbieter",
      "Rechtsgrundlage ändert sich",
      "Neue Aufsichtsbehörde",
      "Material changes to consumer rights"
    ],
    "notRequired": [
      "Redaktionelle Updates",
      "Klarstellungen ohne inhaltliche Änderung",
      "Kontaktinformationen aktualisieren",
      "Sprachliche Anpassungen (AT vs DE)"
    ],
    "versioning": {
      "format": "YYYY-MM-DD",
      "separateVersionsPerJurisdiction": true,
      "globalBumpForAllJurisdictions": "Bei EU-weiten Änderungen (z.B. DSGVO-Update)"
    }
  }
}
```

---

## 🔧 Validierungsskript

**Datei:** `scripts/validate-compliance-rules.py`

Das Skript prüft alle Legal-Dokumente gegen die maschinenlesbaren Regeln:

```bash
# Alle Jurisdiktionen prüfen
python3 scripts/validate-compliance-rules.py

# Nur Österreich prüfen
python3 scripts/validate-compliance-rules.py --jurisdiction AT

# Nur AGB prüfen
python3 scripts/validate-compliance-rules.py --document agb

# JSON-Regeln validieren
python3 scripts/validate-compliance-rules.py --validate-rules
```

---

## 📁 Dateien und Speicherorte

| Datei | Zweck | Pfad |
|-------|-------|------|
| `legal-rules.json` | Maschinenlesbare Compliance-Regeln | `docs/COMPLIANCE/legal-rules.json` |
| `validate-compliance-rules.py` | Validierungsskript | `scripts/validate-compliance-rules.py` |
| `validate-legal-clauses.py` | Klausel-Validierung (existierend) | `scripts/validate-legal-clauses.py` |
| `validate-legal-versions.py` | Versions-Validierung (existierend) | `scripts/validate-legal-versions.py` |

---

## ✅ Checkliste vor Release

### **Rechtssicherheit:**
- [ ] Alle Jurisdiktionen (DE, AT, CZ, EU) abgedeckt
- [ ] Maschinenlesbare Regeln aktuell (legal-rules.json)
- [ ] Validierungsskript läuft fehlerfrei
- [ ] Keine verbotenen Klauseln in Dokumenten
- [ ] Alle mandatoryClauses enthalten

### **Implementation:**
- [ ] LegalConstants.kt um de-at erweitert
- [ ] SUPPORTED_ASSET_LANGUAGES aktualisiert
- [ ] resolveAssetLanguage() routet de-AT → de-at
- [ ] version.txt auf aktuellem Stand

### **Dokumentation:**
- [ ] legal-rules.json vollständig
- [ ] Agent Skill registriert (dieses Dokument)
- [ ] Validierungsskript dokumentiert

---

## 🔗 Wichtige Links

| Ressource | URL |
|-----------|-----|
| **DSGVO (DE)** | https://dsgvo-gesetz.de/ |
| **GDPR Info (EN)** | https://gdpr-info.eu/ |
| **RIS (AT)** | https://www.ris.bka.gv.at/ |
| **ÚOOÚ (CZ)** | https://www.uoou.cz/ |
| **EDPB (EU)** | https://www.edpb.europa.eu/ |
| **DSB (AT)** | https://www.dsb.gv.at/ |
| **LFDI BW (DE)** | https://www.baden-wuerttemberg.datenschutz.de/ |

---

**Stand:** 2026-08-18  
**Version:** 1.0  
**Nächste Prüfung:** Bei Rechtsänderungen oder neuen Dokumenten
