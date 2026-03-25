# Google Play Data Safety - Beemaster

## App-Informationen
- **App-Name:** Beemaster - Bienenverwaltung
- **Paketname:** com.beemaster
- **Kategorie:** Produktivität/Landwirtschaft
- **Entwickler:** Mike Miller

---

## Datenerhebung

### ✅ Vom Nutzer erhobene Daten

| Datentyp | Erforderlich? | Zweck | Weitergabe |
|----------|---------------|-------|------------|
| **Standort (GPS)** | Optional | Standorte der Bienenstöcke auf Karte anzeigen | Keine |
| **Name** | Optional | Imker-Profil personalisieren | Keine |
| **E-Mail** | Optional | Kontakt, Premium-Features | Keine |
| **Telefonnummer** | Optional | Imker-Profil | Keine |
| **Adresse** | Optional | Imker-Standort | Keine |
| **Fotos** | Optional | Bienenstock-Fotos | Keine |
| **Sprachaufnahmen** | Optional | Notizen per Spracheingabe | Keine |

### 🔒 Automatisch erhobene Daten

| Datentyp | Zweck | Weitergabe |
|----------|-------|------------|
| **Crash-Logs** | App-Stabilität verbessern | Firebase Crashlytics (Google) |
| **Nutzungsstatistiken** | App-Verbesserung | Firebase Analytics (Google) |
| **Geräte-ID** | Fehlerdiagnose | Firebase Crashlytics |

### ❌ NICHT erhobene Daten

- Keine Werbe-ID
- Keine Kontaktdaten ohne Einwilligung
- Keine SMS/Nachrichten
- Keine Kalenderdaten
- Keine Browser-Verlauf
- Keine Anrufe
- Keine Gesundheitdaten
- Keine Finanzdaten

---

## Datenspeicherung

### Lokal auf dem Gerät
- **Datenbank:** Room Database (lokal, verschlüsselt)
- **Einstellungen:** DataStore Preferences (lokal)
- **Fotos:** Interner App-Speicher
- **Verschlüsselung:** Android Keystore für sensible Daten

### Cloud/Server
- **Keine Cloud-Speicherung** in der Basis-Version
- **Keine Server-Verbindung** für Nutzerdaten
- **Premium-Features:** Optionaler Sync (separate Vereinbarung)

---

## Drittanbieter

### Firebase (Google)
- **Crashlytics:** Crash-Reporting
- **Analytics:** Anonyme Nutzungsstatistiken
- **Datenschutz:** https://firebase.google.com/support/privacy

### OpenAI API (optional)
- **Zweck:** KI-basierte Imker-Assistenz
- **Nur bei aktiver Nutzung:** Sprach-KI-Features
- **Datenschutz:** https://openai.com/privacy

---

## Berechtigungen

| Berechtigung | Zweck |
|--------------|-------|
| `INTERNET` | fakultative Cloud-Sync |
| `ACCESS_FINE_LOCATION` | GPS-Standorte für Bienenstöcke |
| `ACCESS_COARSE_LOCATION` | Grobe Ortung für Karten |
| `CAMERA` | Fotos von Bienenstöcken |
| `RECORD_AUDIO` | Sprachnotizen |
| `POST_NOTIFICATIONS` | Reminder-Benachrichtigungen |
| `SCHEDULE_EXACT_ALARM` | Reminder-Timer |
| `RECEIVE_BOOT_COMPLETED` | Reminder nach Neustart wiederherstellen |
| `READ_EXTERNAL_STORAGE` |OSMDroid-Kartencache |
| `READ_MEDIA_IMAGES` | Profilbilder |

---

## Kinder- und Jugendschutz

- **App nicht für Kinder unter 13 geeignet**
- **Keine gezielte Datenerhebung bei Kindern**
- **Keine Werbung**
- **Keine In-App-Käufe ohne Altersverifikation**

---

## DSGVO-Konformität (EU)

### Rechtsgrundlage
- **Art. 6 Abs. 1 lit. b DSGVO:** Vertragserfüllung
- **Art. 6 Abs. 1 lit. f DSGVO:** Berechtigtes Interesse (App-Stabilität)
- **Art. 6 Abs. 1 lit. a DSGVO:** Einwilligung (optionale Daten)

### Nutzerrechte
- Auskunft über gespeicherte Daten
- Berichtigung falscher Daten
- Löschung aller Daten
- Datenexport
- Widerruf der Einwilligung

### Kontakt für Datenschutz
- **E-Mail:** privacy@beemaster.app
- **Telegram:** @mightmikemiller

---

## Änderungen

Diese Datenschutzerklärung kann aktualisiert werden. Nutzer werden über wesentliche Änderungen in der App informiert.

**Letzte Aktualisierung:** März 2025

---

## Compiled Answers for Google Play Console

### Werden Nutzerdaten erhoben oder geteilt?
**JA**

### Erforderliche Datentypen:

#### Standort
- **Typ:** Genauer Standort (GPS)folgt:** App-Funktionalität (Bienenstock-Karte)
- **Verschlüsselt:** Ja (in Transit)
- **Kann gelöscht werden:** Ja
- **Geteilt mit:** Keine Dritten

#### Persönliche Informationen
- **Typ:** Name, E-Mail, Telefon (optional)
- **Erforderlich:** Nein (optional)
- **Zweck:** Profil-Personalisierung
- **Verschlüsselt:** Ja (Android Keystore)
- **Kann gelöscht werden:** Ja

#### Fotos und Videos
- **Typ:** Kamera-Aufnahmen
- **Erforderlich:** Nein (optional)
- **Zweck:** Bienenstock-Dokumentation
- **Verschlüsselt:** Ja
- **Kann gelöscht werden:** Ja

#### Audio
- **Typ:** Sprachaufnahmen
- **Erforderlich:** Nein (optional)
- **Zweck:** Notizen per Spracheingabe
- **Kann gelöscht werden:** Ja

#### App-Aktivität
- **Typ:** App-Interaktionen, Crash-Logs
- **Erforderlich:** Nein
- **Zweck:** App-Verbesserung
- **Geteilt mit:** Firebase (Google)

#### Geräte-ID
- **Typ:** Geräteidentifikation
- **Erforderlich:** Ja (für Crash-Reporting)
- **Zweck:** Fehlerdiagnose
- **Geteilt mit:** Firebase Crashlytics

### Daten sicherheitspraktiken:
- ✅ Daten werden verschlüsselt (in Transit)
- ✅ Daten werden verschlüsselt (in Ruhe, Android Keystore)
- ✅ Nutzer können Daten löschen
- ✅ Nutzer können Daten exportieren

### Dritte SDKs:
- **Firebase Crashlytics:** Crash-Reporting
- **Firebase Analytics:** Nutzungsstatistikan (anonym)
- **Google Play Services:** Standortdienste