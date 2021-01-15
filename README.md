# Moodle Logger 
Logge dich mit diesem Programm automatisch in einem von dir bestimmten Zeitintervall in Moodle ein und rufe alle pdf-Dateien in jedem Kurs ab.

## Installation
Benötigt werden:
- Firefox Browser (https://www.mozilla.org/de/firefox/new/)
- win64/win32 Version des Gecko-Webdrivers (https://github.com/mozilla/geckodriver/releases)
  - V.0.28.0 IST IN DIESER REPO SCHON ENTHALTEN, WENN 0.28.0 ALSO DIE NEUSTE VERSION IST, MUSS MAN ES NICHT SELBST HERUNTERLADEN
- logger_UI.exe (in dieser Repo enthalten)

## Benutzung
![](/example.PNG)

- Bei "TESTNUTZERNAME" deinen Moodlenutzernamen eingeben
- Darunter dein Moodlepasswort eingeben
- Bei "OPEN GECKODRIVER" deine geckodriver.exe Datei finden und anklicken
- Beim leeren Feld eine Zeit eingeben (HH:MM:SS oder HH:MM) und auf "ZEIT HINZUFÜGEN" anklicken, um eine spezifische Exekutionszeit hinzuzufügen

Anschließend auf "START" drücken.

## Automatisches Eingeben von Daten
Öffne "logger_UI.cfg" mit einem Textbearbeitungsprogramm.

![](/cfg_example.PNG)

- Bei NUTZERNAME und PASSWORD deinen Moodle - Nutzernamen/Passwort eingeben
- Deine spezifischen Exekutionszeiten des Programms kannst du mit Kommas abgetrennt hinschreiben (HH:MM:SS oder HH:MM)
- "..\dein\pfad" ersetzen durch deinen Pfad zur geckodriver.exe Datei 
