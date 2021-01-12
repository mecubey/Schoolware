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

- Bei "MOODLE_USERNAME" deinen Moodlenutzernamen eingeben
- Bei "MOODLE_PASSWORT" dein Moodlepasswort eingeben
- Bei "INTERVAL EINFÜGEN" deinen gewünschten Zeitintervall eingeben
  - dass heißt, das nach jeder erfolgreichen/erfolgslosen Iteration des Programms, sich das Programm nach deinem eingefügten Interval wiederholt
- Bei "OPEN GECKODRIVER" deine geckodriver.exe Datei finden und anklicken

Anschließend auf "START" drücken.
