# Aplikacja Pomagająca w Rozwiązywaniu Zadań na Kolokwium z Przedmiotu ARCHI

To repozytorium zawiera aplikację napisaną w Pythonie z użyciem Tkinter, która pomaga w rozwiązywaniu zadań na kolokwium z przedmiotu ARCHI. Aplikacja oferuje interaktywny interfejs graficzny, który umożliwia użytkownikom łatwe wprowadzanie danych i obliczanie wyników dla różnych typów zadań.

## Funkcje Aplikacji

- **Zadanie 1:** Oblicza liczbę par SEGMENT:OFFSET dla podanej wartości RAM.
- **Zadanie 2:** Oblicza wartość rejestru AX w porównaniu do BX.
- **Zadanie 3:** Oblicza liczbę par dla podanej wartości RAM.
- **Zadanie 4:** Oblicza wartość dziesiętną adresu fizycznego komórki pamięci RAM.
- **Zadanie 5:** Oblicza wartość rejestru SP po wykonaniu operacji.

## Wymagania

- Python 3.x
- Tkinter (zazwyczaj zainstalowany domyślnie z Pythonem)
- ffmpeg (jeśli chcesz konwertować pliki wideo, choć nie jest to część tego konkretnego programu)

## Instalacja

1. **Sklonuj to repozytorium:**
    ```sh
    git clone https://github.com/twoje-nazwa-uzytkownika/archi-helper.git
    cd archi-helper
    ```

2. **Zainstaluj wymagane pakiety (jeśli to konieczne):**
    Jeśli nie masz Tkinter, możesz zainstalować go za pomocą menedżera pakietów odpowiedniego dla twojego systemu operacyjnego.

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

## Przykład

![Example Screenshot](screenshot.png)

## Wsparcie

Jeśli masz jakiekolwiek pytania lub napotkałeś problemy, otwórz nowy problem w zakładce Issues na GitHubie.

## Licencja

Ten projekt jest licencjonowany na zasadach licencji MIT. Zobacz plik [LICENSE](LICENSE) po więcej informacji.
