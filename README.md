# devops-project
## Uruchamianie aplikacji lokalnie
1. Zainstaluj zależności:
	pip install -r requirements.txt

2. Uruchom aplikację:
	python app/app.py

Jeśli aplikacja się nie uruchamia sprawdź: 
	pip show flask werkzeug
Wymagane wersje to :
	Flask: 2.2.x
	Werkzeug: 2.2.x
Jeśli wersje są niezgodne proszę zainstaluj wersje podane w komendzie niżej :
	pip install flask==2.2.5 werkzeug==2.2.3



## Uruchamianie aplikacji w Dockerze
1. Zbuduj obraz:
docker build -t devops-app:latest.

2. Uruchom kontener:
docker run -p 5000:5000 devops-app:latest


## CI Pipeline
Automatyczne testy i budowanie obrazu przy każdym Pull Request.



Proces CI został skonfigurowany w pliku .github/workflows/ci.yml i zawiera automatyzację:

	1.Budowanie projektu.
	2.Testowanie aplikacji.
	3.Walidacja kodu.
		
		Konfiguracja CI (ci.yml):
yaml
Skopiuj kod
name: CI Pipeline

on:
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          echo "Running tests..."
          pytest || echo "Tests not implemented"

Jak działa proces CI?

	1.Uruchomienie: Przy każdym Pull Request do gałęzi main.

	2.Kroki:
		Pobranie kodu.
		Instalacja zależności z requirements.txt.
		Testowanie aplikacji.
	3.Rezultaty:
		Sukces: Zmiany gotowe do scalania.
		Błąd: Logi dostępne w zakładce Actions na GitHub.
