# Beemaster - Google Play Console Datenschutzangaben

## Schnellausfüllhilfe für Google Play Console

---

## Schritt 1: Werden Nutzerdaten erhoben oder geteilt?
**Antwort: JA**

---

## Schritt 2: Datentypen auswählen

### ✅ Standort
- **Genauer Standort (GPS):** JA
- **Ungefährer Standort:** JA  
- **Im Hintergrund:** NEIN
- **Erforderlich:** NEIN (optional, für Kartenfunktion)
- **Zweck:** App-Funktionalität
- **Geteilt mit Dritte:** NEIN

### ✅ Persönliche Informationen
- **Name:** JA (optional)
- **E-Mail-Adresse:** JA (optional)
- **Telefonnummer:** JA (optional)
- **Adresse:** JA (optional)
- **Erforderlich:** NEIN
- **Zweck:** App-Funktionalität (Profil)
- **Geteilt mit Dritte:** NEIN

### ✅ Fotos und Videos
- **Kamera:** JA (optional)
- **Bilder:** JA (optional)
- **Erforderlich:** NEIN
- **Zweck:** App-Funktionalität (Bienenstock-Doku)
- **Geteilt mit Dritte:** NEIN

### ✅ Audio
- **Sprachaufnahmen:** JA (optional)
- **Erforderlich:** NEIN
- **Zweck:** App-Funktionalität (Notizen)
- **Geteilt mit Dritte:** NEIN

### ✅ App-Aktivität
- **App-Interaktionen:** NEIN
- **In-App-Suche:** NEIN
- **Installierte Apps:** NEIN

### ✅ App-Informationen und Leistung
- **Crash-Logs:** JA
- **Diagnose:** JA
- **Erforderlich:** NEIN
- **Zweck:** App-Stabilität
- **Geteilt mit Dritte:** JA (Firebase Crashlytics)

### ✅ Geräte-ID
- **Geräte-ID oder andere Kennungen:** JA
- **Erforderlich:** JA (für Crash-Reporting)
- **Zweck:** Fehlerdiagnose, App-Stabilität
- **Geteilt mit Dritte:** JA (Firebase)

### ❌ NICHT ausgewählte Datentypen:
- Finanzinformationen
- Gesundheit und Fitness
- Nachrichten
- SMS
- Kalender
- Kontakte
- Benutzerdefinierte Daten
- Web-Browsing
- Bluetooth
- Netzwerk
- Telefonanrufe
- WLAN-Verbindungen

---

## Schritt 3: Datensicherheitspraktiken

### ✅ Auswählen:
- [x] Daten werden verschlüsselt während der Übertragung
- [x] Daten werden verschlüsselt im Ruhezustand
- [x] Nutzer können Daten löschen
- [x] Nutzer können Daten exportieren
- [ ] Daten werden unabhängig geprüft (optional)
- [ ] Daten werden mit Tools geprüft, die Eltern bei der Überwachung unterstützen (nicht zutreffend)

---

## Schritt 4: Wer erhält die Daten?

### App-Entwickler (Mike Miller)
Datentypen: Alle lokalen Daten

### Dienstleister:
**Firebase (Google)**
- Crashlytics (Crash-Logs)
- Analytics (anonyme Nutzungsdaten)
- Standort: USA
- Webseite: firebase.google.com

---

## Schritt 5: URL für Datenschutzrichtlinie

**URL:** https://l33ttoolbot.github.io/beemaster-privacy/

(Hinweis: Diese URL muss noch erstellt werden)

---

## Zusammenfassung für Copy-Paste

### Kurze Beschreibung (80 Zeichen):
"Beemaster verwaltet deine Bienenstöcke lokal - deine Daten bleiben bei dir."

### Lange Beschreibung:
"Beemaster ist die professionelle Bienenverwaltungs-App für Imker. alle Daten werden lokal auf deinem Gerät gespeichert. Mit GPS-Standortverfolgung für deine Bienenstöcke, Foto-Dokumentation und Sprachnotizen. Keine云端-Speicherung, keine Werbung, maximaler Datenschutz."

---

## Google Play Store-Eintrag

### Kategorie:
Produktivität

### Altersfreigabe:
Alle Altersgruppen (IAP: keine)

### Datenschutz-URL:
https://l33ttoolbot.github.io/beemaster-privacy/

---

## Hinweise für den Entwickler

1. **Firebase deaktivieren:** Falls du Firebase Analytics/Crashlytics nicht verwendest, entferne die Abhängigkeiten aus build.gradle.kts

2. **Verschlüsselung:** Die PrivacySettings.kt zeigt bereits Android Keystore-Verschlüsselung - gut!

3. **Datenschutzerklärung hosten:** Die HTML-Datei muss auf einer öffentlichen URL verfügbar sein

4. **Regelmäßige Updates:** Bei Änderungen an Berechtigungen oder SDKs musst du die Angaben aktualisieren