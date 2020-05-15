# Strona internetowa firmy windykacyjnej
#### Projekt na zaliczenie

Informacje:
* Przedmiot:  Zaawansowane języki skryptowe 
* Kierunek: Informatyka
* Wydział: Matematyki, Fizyki i Informatyki
* Uniwersytet: Gdański
* Język: Python 3
* Framework: Django
* Rok: 2020

#### Opis
Strona korzysta z Cross Site Request Forgery protection, logowanie odbywa się poprzez aplikację (nie w sekcji admin)
obowiązuje walidacja danych wprowadzanych do tabel .

## CRUD

### CREATE
* Możliwość dodawania pracowników, oprócz pól podstawowych dodana jest relacja jeden do jednego z dodatkowymu polami (tylko jako admin)
* Możliwość dodawania spraw, powiązanie relacją jeden do wielu z dokumentami, oraz wiele do jednego z windykatorami (tylko jako admin)
* Możliwość dodawania dokumentów, powiązanie relacją wiele do jednego ze sprawami (tylko jako admin)

### READ
* Przeglądanie treści jest możliwe tylko po zalogowaniu 

### UPDATE
* Możliwość edycji pracownika (tylko jako admin)

### DELETE
* Możliwość usunięcia pracownika (tylko jako admin)
* Możliwość usunięcia sprawy 
* Możliwość usunięcia dokumentów

