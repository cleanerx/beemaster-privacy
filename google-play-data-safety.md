# Google Play Data Safety — Beemaster (v2, Stand 2026-11-23)

**Gültige Quelle:** Datenschutzerklärung **3.9 (2026-11-23)** in der App und auf
`https://beemaster-app.de/` (dieselben Texte, Render-Gate geprüft).
**Entwickler/Kontakt:** Jens Kübler · support@dolphincrusher.com (nicht „Mike Miller" — der alte
Bogen war veraltet).

Diese Datei ist der **Ausfüll-Leitfaden** für das Play-Console-Formular
„Datenicherheit". Regel: Die Angaben müssen zur Datenschutzerklärung passen
(Disclosure-Gate prüft Code ↔ DSE; dieses Blatt prüft DSE ↔ Play-Formular).

Play-Definitionen: **„Erhoben"** = Daten verlassen das Gerät (an uns oder Auftragsverarbeiter).
**„Weitergegeben"** = Übergabe an **unabhängige Verantwortliche** (Auftragsverarbeiter zählen
**nicht** als Weitergabe). **Temporär** = nur flüchtig im Speicher/Prozess, nicht persistiert.

---

## 1. Übersicht: Was wird erhoben?

| Play-Kategorie | Erhoben? | Weitergegeben? | Dauer | Zweck(e) |
|---|---|---|---|---|
| Persönliche Daten → **E-Mail** | Ja (optional, Konto) | Nein | gespeichert (bis Löschung) | App-Funktionalität, Kontoverwaltung |
| Persönliche Daten → **Name/Anzeigename** | Ja (optional, nur Google-Sign-in) | Nein | gespeichert | App-Funktionalität |
| App-Aktivitäten → **App-Interaktionen** | Ja (opt-in) | Nein | gespeichert (Retention 3 J) | Analyse (Fehlerbehebung) |
| App-Aktivitäten → **App-Fehler und Diagnose** | Ja (opt-in) | Nein | gemäß Firebase-Retention | Analyse, App-Funktionalität |
| Geräte-/sonstige **IDs** | Ja (pseudonym) | Nein | gespeichert | App-Funktionalität, Analyse, Betrugsprävention |
| **Audio** | Ja (optional, Funktion) | Nein | **temporär** (STT/TTS-Verarbeitung) | App-Funktionalität |
| **Fotos** | Ja (optional) | Nein | gespeichert (lokales + verschlüsseltes Cloud-Backup) | App-Funktionalität |
| **Standort (genau/ungefähr)** | Ja (optional) | **Ja** | gespeichert (Standorte) / temporär (Wetter) | App-Funktionalität |
| **Finanzdaten → Kaufhistorie** | Ja | **Ja (Google)** | gespeichert | App-Funktionalität, Betrugsprävention, Recht |
| Nutzerinhalte → **Andere Inhalte** (Notizen, Beute-/Schwarmdaten, KI-Chat) | Ja (optional, Sync/Chat) | Nein | gespeichert | App-Funktionalität |
| **Nicht erhoben:** Werbe-ID (AD_ID/SSAID **deaktiviert**), Telefonnummer, Adresse, Gesundheitsdaten, Browser-Verlauf, Kontakte, Werbung | — | — | — | — |

## 2. Weitergabe an unabhängige Verantwortliche (das Feld „Weitergegeben: Ja")

| Empfänger | Daten | Warum unabhängiger Verantwortlicher |
|---|---|---|
| **Google (Play Billing / Google Commerce Ltd.)** | Kauf-Token, Produkt-ID, App-/Geräteangaben | Merchant of Record; Abrechnung läuft über Google |
| **Google (OAuth, nur bei Google-Sign-in)** | Google-Konto-Kennung (Anmeldung) | Google als Identitäts-Provider |
| **CARTO** (Kartenkacheln) | IP-Adresse + angeforderte Kacheln (implizit Koordinaten) | Eigener Dienst, empfängt Anfragen direkt |
| **Nationale Wetterdienste** (DWD/CHMI/HungaroMet/IMGW/SHMÚ/MeteoSwiss) | Standortangabe (Ort/Koordinaten der Abfrage), IP | Eigene APIs, empfangen Abfragen direkt |

Auftragsverarbeiter (zählen **nicht** als „Weitergegeben"): Supabase (Hosting/Auth/DB,
EU/Irland), Microsoft **Azure AI Speech** (STT/TTS, EU/Schweden), **Mistral AI** (LLM, EU/Frankreich,
kein Training), **Brevo** (transaktionale Konto-Mails, EU/Frankreich), **Scaleway** (verschlüsselte
Cloud-Backups, EU/Frankreich), **Netcup** (Hosting, DE).

## 3. Datenschutzpraktiken (Formular-Abschnitt „Praktiken")

- **Verschlüsselung während der Übertragung:** Ja (alles TLS; Sync/Backups zusätzlich AES-256-GCM).
- **Mechanismus für Löschanforderungen:** Ja (Kontolöschung in-App, Art. 17; Datenexport vorab möglich).
- **Zielgruppe Kinder:** Nein — App richtet sich nicht an Kinder; Zielgruppe 13+.
- **Unabhängiger Datenschutz-Dienstleister für Werbezwecke:** Nein (keine Werbung, keine Ad-ID).

## 4. Formular-Führung (Play Console)

Pfad (neue Console): **„Mit Google Play geschützt" / App-Inhalt → Datenicherheit → Verwalten**.

1. **Datenschutzrichtlinie-URL:** `https://beemaster-app.de/` (aktuelle Fassung 3.9).
2. **Sammeln/Weitergeben:** „Ja, es werden Nutzerdaten erhoben und weitergegeben."
3. **Kategorien** gemäß Tabelle oben; pro Kategorie: Typ ankreuzen, optional/erforderlich,
   temporär (nur Audio-Verarbeitung), Zweck-Tags:
   - E-Mail/Name/Konto → **App-Funktionalität**, **Kontoverwaltung**; Weitergabe nein.
   - App-Interaktionen/App-Fehler/IDs → **Analyse**, **App-Funktionalität**, **Betrugsprävention**;
     opt-in (standardmäßig deaktiviert), Weitergabe nein (Firebase = Auftragsverarbeiter).
   - Audio → **App-Funktionalität**, temporär, Weitergabe nein (Azure/Mistral = AVV).
   - Standort → **App-Funktionalität**; Weitergabe **ja** (CARTO, Wetterdienste).
   - Kaufhistorie → **App-Funktionalität**, **Betrugsprävention**; Weitergabe **ja** (Google = MoR).
   - Fotos/Andere Inhalte → **App-Funktionalität**; Weitergabe nein.
4. **Praktiken** wie Abschnitt 3.
5. **Speichern + Formular einreichen** (gilt app-weit; neue Versionen müssen kompatibel bleiben).

## 5. Wichtige Abgrenzungen (bewusst NICHT deklariert)

- **Mollie** (alternative Zahlung): nur in Test-Builds aktiv, im Production-Build inaktiv
  (Aktivierung erst nach Google-Freischaltung) → im Formular **nicht** deklarieren;
  bei Aktivierung nachtragen.
- **Werbe-ID:** AD_ID- und AdServices-Berechtigungen sind via `tools:node="remove"` entfernt;
  Firebase-Flags (`google_analytics_adid_collection_enabled=false`,
  `google_analytics_ssaid_collection_enabled=false`) → keine Deklaration „Werbung/IDs zu Marketing".
- **Firebase:** standardmäßig deaktiviert, Erhebung nur nach opt-in-Einwilligung (DSE 6.1).
- **ML-Kit Belegerkennung:** vollständig on-device, keine Übermittlung → keine Deklaration.

## 6. Nachweis

- Datenschutzerklärung 3.9 (18 Sprachen): App-Assets + `https://beemaster-app.de/` (Render-Gate).
- Disclosure-Gate: `beemaster-process/scripts/check-processor-disclosure.py` (Code ↔ DSE).
- Consent-Nachweis: EULA/AGB/DSE-Akzeptanz mit Versions-Hash (Art. 7 Abs. 1).
