#!/usr/bin/env python3
"""
Validiert Legal-Dokumente gegen maschinenlesbare Compliance-Regeln.

Verwendung:
    python3 scripts/validate-compliance-rules.py [--jurisdiction DE|AT|CZ|EU] [--document agb|eula|privacy|impressum] [--validate-rules]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
RULES_FILE = PROJECT_ROOT / "docs" / "COMPLIANCE" / "legal-rules.json"
LEGAL_ASSETS_DIR = PROJECT_ROOT  # Flat structure in privacy repo


def load_rules() -> dict[str, Any]:
    """Lädt die maschinenlesbaren Compliance-Regeln."""
    if not RULES_FILE.exists():
        print(f"❌ Regeln-Datei nicht gefunden: {RULES_FILE}")
        sys.exit(1)
    
    with open(RULES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_document_content(jurisdiction: str, document: str) -> str:
    """Liest den Inhalt eines Legal-Dokuments (privacy repo flat structure)."""
# Privacy repo uses flat structure: agb_at.html, privacy_at.html, etc.
    suffix_map = {
        "DE": "",
        "AT": "_at",
        "CZ": "_cs",
        "EU": "_en",
        "HU": "_hu",
        "PL": "_pl",
        "SK": "_sk",
        "BG": "_bg",
        "LU": "_lu",
        "FR": "_fr",
        "BE": "_be",
        "BE-NL": "_be-nl",
        "NL": "_nl",
        "DA": "_da",
        "IT": "_it"
    }
    suffix = suffix_map.get(jurisdiction, "")

    # Privacy repo uses index.html for DE privacy, privacy_at.html for AT, etc.
    doc_file_map = {
        "DE": {"agb": "agb.html", "eula": "eula.html", "privacy": "index.html", "impressum": "impressum.html"},
        "AT": {"agb": "agb_at.html", "eula": "eula_at.html", "privacy": "privacy_at.html", "impressum": "impressum_at.html"},
        "CZ": {"agb": "agb.html", "eula": "eula.html", "privacy": "privacy_cs.html", "impressum": "impressum.html"},
        "EU": {"agb": "agb_en.html", "eula": "eula_en.html", "privacy": "privacy_en.html", "impressum": "impressum_en.html"},
        "HU": {"agb": "agb_hu.html", "eula": "eula_hu.html", "privacy": "privacy_hu.html", "impressum": "impressum_hu.html"},
        "PL": {"agb": "agb_pl.html", "eula": "eula_pl.html", "privacy": "privacy_pl.html", "impressum": "impressum_pl.html"},
        "SK": {"agb": "agb_sk.html", "eula": "eula_sk.html", "privacy": "privacy_sk.html", "impressum": "impressum_sk.html"},
        "BG": {"agb": "agb_bg.html", "eula": "eula_bg.html", "privacy": "privacy_bg.html", "impressum": "impressum_bg.html"},
        "LU": {"agb": "agb_lu.html", "eula": "eula_lu.html", "privacy": "privacy_lu.html", "impressum": "impressum_lu.html"},
        "FR": {"agb": "agb_fr.html", "eula": "eula_fr.html", "privacy": "privacy_fr.html", "impressum": "impressum_fr.html"},
        "BE": {"agb": "agb_be.html", "eula": "eula_be.html", "privacy": "privacy_be.html", "impressum": "impressum_be.html"},
        "BE-NL": {"agb": "agb_be-nl.html", "eula": "eula_be-nl.html", "privacy": "privacy_be-nl.html", "impressum": "impressum_be-nl.html"},
        "NL": {"agb": "agb_nl.html", "eula": "eula_nl.html", "privacy": "privacy_nl.html", "impressum": "impressum_nl.html"},
        "DA": {"agb": "agb_da.html", "eula": "eula_da.html", "privacy": "privacy_da.html", "impressum": "impressum_da.html"},
        "IT": {"agb": "agb_it.html", "eula": "eula_it.html", "privacy": "privacy_it.html", "impressum": "impressum_it.html"}
    }
    
    doc_file = doc_file_map.get(jurisdiction, {}).get(document, f"{document}{suffix}.html")
    file_path = LEGAL_ASSETS_DIR / doc_file
    
    if not file_path.exists():
        return ""
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def validate_rule(content: str, rule: dict) -> tuple[bool, str]:
    """
    Prüft eine einzelne Regel gegen den Dokumenteninhalt.
    
    Returns: (passed, message)
    """
    patterns = rule.get("patterns", [])
    check_type = rule.get("check", "contains")
    
    if check_type == "contains":
        for pattern in patterns:
            if pattern.lower() in content.lower():
                return True, f"✓ Pattern '{pattern}' gefunden"
        return False, f"✗ Keines der Patterns gefunden: {patterns}"
    
    elif check_type == "notContains":
        for pattern in patterns:
            if pattern.lower() in content.lower():
                return False, f"✗ Verbotenes Pattern gefunden: '{pattern}'"
        return True, f"✓ Keine verbotenen Patterns gefunden"
    
    return True, "✓ Regel nicht anwendbar"


def validate_jurisdiction(jurisdiction: str, rules_data: dict) -> list[str]:
    """Validiert alle Dokumente einer Jurisdiktion (privacy repo flat structure)."""
    errors = []
    jur_data = rules_data["jurisdictions"].get(jurisdiction)
    
    if not jur_data:
        errors.append(f"❌ Jurisdiktion '{jurisdiction}' nicht in Regeln gefunden")
        return errors
    
    # Privacy repo uses flat structure, no folders
    print(f"\n📋 Validiere Jurisdiktion: {jurisdiction}")
    print("=" * 60)
    
    documents = ["agb", "eula", "privacy", "impressum"]
    
    for doc in documents:
        content = get_document_content(jurisdiction, doc)
        
        if not content:
            errors.append(f"⚠️  Dokument '{doc}' nicht gefunden oder leer")
            continue
        
        print(f"\n  Dokument: {doc}.html")
        
        applicable_rules = [
            r for r in rules_data.get("validationRules", [])
            if jurisdiction in r.get("appliesTo", []) and 
               (r.get("document") == doc or r.get("document") == "all")
        ]
        
        for rule in applicable_rules:
            passed, message = validate_rule(content, rule)
            severity = rule.get("severity", "ERROR")
            
            if passed:
                print(f"    ✓ {rule['id']}: {message}")
            else:
                error_msg = f"    {severity} {rule['id']}: {message}"
                print(error_msg)
                if severity == "ERROR":
                    errors.append(error_msg)
    
    return errors


def validate_rules_structure(rules_data: dict) -> list[str]:
    """Validiert die Struktur der Regeln-JSON."""
    errors = []
    
    required_keys = ["version", "jurisdictions", "validationRules", "reConsentRules"]
    for key in required_keys:
        if key not in rules_data:
            errors.append(f"❌ Fehlender Schlüssel in legal-rules.json: {key}")
    
    if "jurisdictions" in rules_data:
        for jur_id in rules_data["jurisdictions"]:
            jur = rules_data["jurisdictions"][jur_id]
            if "assetFolder" not in jur:
                errors.append(f"❌ Jurisdiktion {jur_id} fehlt 'assetFolder'")
            if "mandatoryClauses" not in jur:
                errors.append(f"❌ Jurisdiktion {jur_id} fehlt 'mandatoryClauses'")
    
    if "validationRules" in rules_data:
        for i, rule in enumerate(rules_data["validationRules"]):
            if "id" not in rule:
                errors.append(f"❌ Regel {i} fehlt 'id'")
            if "check" not in rule:
                errors.append(f"❌ Regel {i} fehlt 'check'")
            if "patterns" not in rule:
                errors.append(f"❌ Regel {i} fehlt 'patterns'")
    
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validiert Legal-Dokumente gegen Compliance-Regeln")
    parser.add_argument("--jurisdiction", choices=["DE", "AT", "CZ", "EU", "HU", "PL", "SK", "BG", "LU", "FR", "BE", "BE-NL", "NL", "DA", "IT", "ALL"], default="ALL",
                        help="Zu prüfende Jurisdiktion (Default: ALL)")
    parser.add_argument("--document", choices=["agb", "eula", "privacy", "impressum"],
                        help="Zu prüfendes Dokument (nur mit --jurisdiction)")
    parser.add_argument("--validate-rules", action="store_true",
                        help="Validiert die Struktur der legal-rules.json")
    
    args = parser.parse_args()
    
    print("🔍 Legal Compliance Rules Validator")
    print("=" * 60)
    print(f"Regeln: {RULES_FILE}")
    print(f"Assets: {LEGAL_ASSETS_DIR}")
    
    rules_data = load_rules()
    print(f"Regeln-Version: {rules_data.get('version', 'unbekannt')}")
    
    all_errors = []
    
    if args.validate_rules:
        print("\n📋 Validiere Regeln-Struktur...")
        print("=" * 60)
        struct_errors = validate_rules_structure(rules_data)
        all_errors.extend(struct_errors)
        if not struct_errors:
            print("✓ Regeln-Struktur ist gültig")
    
    jurisdictions = list(rules_data.get("jurisdictions", {}).keys()) if args.jurisdiction == "ALL" else [args.jurisdiction]
    
    for jur in jurisdictions:
        if args.document:
            jur_data = rules_data["jurisdictions"].get(jur, {})
            asset_folder = jur_data.get("assetFolder", jur.lower())
            doc_file = {"agb": "agb.html", "eula": "eula.html", "privacy": "datenschutz.html", "impressum": "impressum.html"}.get(args.document, args.document)
            
            content = get_document_content(jur, args.document)
            if not content:
                all_errors.append(f"❌ Dokument {asset_folder}/{doc_file} nicht gefunden")
                continue
            
            print(f"\n📋 Validiere {jur} / {args.document}.html")
            print("=" * 60)
            
            applicable_rules = [
                r for r in rules_data.get("validationRules", [])
                if jur in r.get("appliesTo", []) and 
                   (r.get("document") == args.document or r.get("document") == "all")
            ]
            
            for rule in applicable_rules:
                passed, message = validate_rule(content, rule)
                severity = rule.get("severity", "ERROR")
                if not passed:
                    error_msg = f"{severity} {rule['id']}: {message}"
                    print(error_msg)
                    if severity == "ERROR":
                        all_errors.append(error_msg)
                else:
                    print(f"✓ {rule['id']}: {message}")
        else:
            errors = validate_jurisdiction(jur, rules_data)
            all_errors.extend(errors)
    
    print("\n" + "=" * 60)
    if all_errors:
        print(f"❌ Validierung FEHLGESCHLAGEN: {len(all_errors)} Fehler")
        for error in all_errors:
            print(error)
        sys.exit(1)
    else:
        print("✅ Validierung ERFOLGREICH: Alle Regeln erfüllt")
        sys.exit(0)


if __name__ == "__main__":
    main()
