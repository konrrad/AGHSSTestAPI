## Test API for AGH Space Systems

Bazą jest MongoDB(bo JSON), działa w chmurze.

W configuration.py są parametry połączenia - port można zmienić.

### Endpointy
- /getAll - zwraca odpowiedz w formacie JSON zawierajaca wszystkie dane z bazy,
- /getOne/:id - zwraca pojedynczy test o podanym w parametrze id,
- /addOne - dodaje pojedynczy plik do bazy danych,
- /delete/:id - usuwa pojedynczy pliku o podanym w parametrze id.


### Uruchomienie
`pip3 install -r requrements.txt`

`python3 app.py`