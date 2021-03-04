# Raporty GLPI

## Spis treści

  * [Informacje ogólne](#informacje-ogólne)
    * [Założenia [WSZ]](#założenia-[wsz])
    * [Założenia [WSP]](#założenia-[wsp])
  * [Technologie](#technologie)
  * [Konfiguracja](#konfiguracja)
  * [Instalacja zależności](#instalacja-zależności)

## Informacje ogólne

Moduł pozwoli pobierać informacje z systemu GLPI na temat poświeconego czasu na zadania ze zgłoszeń oraz zadań powiązanych z projektami w zadanym zakrecie dat. Czasy zostaną zsumowane dla odpowiedniego technika. Celem będzie wykazanie dwóch wskaźników:
* Wskaźnik poświęconego czasu na zgłoszenia [WSZ]
* Wskaźnik poświęconego czasu na projety [WSP]

##### Założenia [WSZ]:
* czasy tylko pracowników działu IT
* zadania zgłoszeń przypisane do projektów nie będą zaliczane
* jedynie zakończone zadanie będą sumowane (niezależnie od statusu zgłoszemia)
* wyznacznikiem warunku czasowego będzie data modyfikacji __(uwaga zadanie zakończone dalej można modyfikować na niezakończonym zgłoszeniu)__

##### Założenia [WSP]:
* czasy tylko pracowników działu IT
* czas zostanie zaliczony każdemu pracownikowi przysanemu do zespołu zadania
* poza czasami zadań projektu będą też zaliczane czasy zadań zgłoszeń przypisanych do projektu _(czasy zadań w takim zgłoszeniu bedą dodane odpowiedni każdemu pracownikowi)_
* jedynie zakończone zadanie będą sumowane (niezależnie od stanu projektu)
* wyznacznikiem warunku czasowego będzie data modyfikacji __(uwaga zadanie zakończone dalej można modyfikować na niezakończonym projekcie)__

## Technologie

Projekt tworzony jest za pomocą:

* Python: 3.8
  * PyMySQL: 1.0.2

## Konfiguracja

Aby uruchomić wystarczy:

```bash
$ python make_reports.py 
Ban----- Michał         --> 12.2500
Bilk------ Marcin       --> 23.0000
Chr------ Grzegorz      --> 5.0000
Juch------- Kamil       --> 24.7500
```

## Instalacja zależności

Przykład na dystrybucji linuxa Debian:

```
$ sudo apt install python3.8 python3.8-pip
$ pip install pipenv

$ git clone https://github.com/kjuchniewicz/RaportGLPI.git
$ cd RaportGLPI

$ pipenv install
$ pipenv shell

$ python make_reports.py
```
