# Aplikacja Pomagająca w Rozwiązywaniu Zadań z ARCHI

To repozytorium zawiera aplikację napisaną w Pythonie, która pomaga w rozwiązywaniu ARCHI. Aplikacja oferuje interaktywny interfejs graficzny, który umożliwia łatwe wprowadzanie danych i obliczanie wyników dla różnych typów zadań.

## Funkcje Aplikacji

- **Zadanie 1:** Oblicza liczbę par SEGMENT:OFFSET dla podanej wartości RAM.
- **Zadanie 2:** Oblicza wartość rejestru AX w porównaniu do BX.
- **Zadanie 3:** Oblicza liczbę par dla podanej wartości RAM.
- **Zadanie 4:** Oblicza wartość dziesiętną adresu fizycznego komórki pamięci RAM.
- **Zadanie 5:** Oblicza wartość rejestru SP po wykonaniu operacji.

## Wymagania

- Python 3.x
- Tkinter (zazwyczaj zainstalowany domyślnie z Pythonem)

## Instalacja

1. **Sklonuj to repozytorium:**
    ```sh
    git clone https://github.com/aradinjp/Kolos-ARCHI.git ./kolos-archi-help
    cd kolos-archi-help
    ```

2. **Zainstaluj wymagane pakiety (jeśli to konieczne):**

    ### Instalacja Tkinter:

    Tkinter jest zazwyczaj domyślnie zainstalowany z Pythonem, ale jeśli go nie masz, możesz go zainstalować w zależności od twojego systemu operacyjnego:

    **Windows:**
    Tkinter powinien być zainstalowany domyślnie. Jeśli nie, możesz zainstalować go poprzez instalację najnowszej wersji Pythona z [python.org](https://www.python.org/downloads/).

    **macOS:**
    Użyj Homebrew, aby zainstalować Tkinter:
    ```sh
    brew install python-tk
    ```

    **Linux (Debian/Ubuntu):**
    Możesz zainstalować Tkinter za pomocą apt:
    ```sh
    sudo apt-get install python3-tk
    ```

    **Linux (Fedora):**
    Możesz zainstalować Tkinter za pomocą dnf:
    ```sh
    sudo dnf install python3-tkinter
    ```
3. **Uruchom aplikację:**
    ```sh
    python main.py
    ```

## Użycie

1. Uruchom aplikację za pomocą polecenia `python main.py`.
2. W interfejsie graficznym wybierz zadanie, które chcesz rozwiązać.
3. Wprowadź wymagane dane w odpowiednich polach tekstowych.
4. Kliknij przycisk "Oblicz" obok zadania, aby uzyskać wynik.
5. Użyj przycisku "Reset", aby wyczyścić wszystkie pola i wyniki.

## Wsparcie

Jeśli masz jakiekolwiek pytania lub napotkałeś problemy, otwórz nowy problem w zakładce Issues na GitHubie.

## Licencja

Ten projekt jest licencjonowany na zasadach licencji MIT. Zobacz plik [LICENSE](LICENSE) po więcej informacji.
