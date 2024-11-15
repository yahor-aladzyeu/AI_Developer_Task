## Konfiguracja
1. Ustaw klucz API OpenAI jako zmienną środowiskową lub bezpośrednio w kodzie, np. `api_key = 'YOUR_API_KEY'`.
2. Umieść plik wejściowy z treścią artykułu (`Zadanie dla Junior AI Developera - tresc artykulu.txt`) w katalogu projektu lub zaktualizuj ścieżkę do pliku w kodzie.

## Uruchomienie aplikacji
Aby uruchomić aplikację, użyj następującej komendy:
```bash
python main.py
## Project Structure

- `main.py` – Main application script for processing the article.
- `README.md` – Project documentation and instructions.
- `artykul.html` – The generated HTML file containing the processed article content.

## Szczegóły kodu

### Importowanie bibliotek
Kod korzysta z biblioteki OpenAI do komunikacji z modelem GPT-4 i generowania HTML na podstawie tekstu artykułu.

```python
import openai

### Inicjalizacja klienta OpenAI

Klient OpenAI jest inicjalizowany przy użyciu klucza API:

```python
client = openai.Client(api_key='YOUR_API_KEY')
### Funkcja `get_openai_response`

Funkcja `get_openai_response` tworzy zapytanie do OpenAI z użyciem wybranego modelu (GPT-4). Zadaniem tej funkcji jest przetworzenie tekstu artykułu i wygenerowanie kodu HTML. Funkcja oczekuje promptu, który zawiera treść artykułu, a odpowiedź jest limitowana do 1024 tokenów:

```python
def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Generate HTML content for the following article text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()
### Przetwarzanie pliku wejściowego

Aplikacja odczytuje zawartość pliku tekstowego z artykułem. Plik ten jest załadowany jako ciąg znaków, który następnie przekazywany jest do funkcji `get_openai_response` w celu przekształcenia go na format HTML:

```python
input_file_path = 'D:/OXIDO/Oxido - Project/Zadanie dla Junior AI Developera - tresc artykulu.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    article_text = file.read()
### Przygotowanie promptu dla OpenAI

Prompt zawiera instrukcję przekształcenia tekstu na format HTML oraz dodania miejsc na grafikę. W tekście artykułu, w określonych miejscach, sugerowane są obrazy, co jest odzwierciedlone w prompt:

```python
prompt = f"Przeformatuj ten tekst jako HTML, uwzględniając miejsca na grafikę: {article_text}"
### Generowanie i zapisanie HTML

Po wygenerowaniu treści HTML przez OpenAI, kod zapisuje wynik w pliku `artykul.html`:

```python
html_content = get_openai_response(prompt)

output_file_path = 'D:/OXIDO/Oxido - Project/artykul.html'
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML generated and saved in the file 'artykul.html'.")
Plik HTML zawiera treść artykułu z odpowiednimi nagłówkami (<h1>, <h2>), akapitami (<p>), oraz miejscami na obrazy (<img src="image_placeholder.jpg" alt="Opis obrazu">).
## Wynik

Wygenerowany plik HTML (`artykul.html`) będzie zapisany w katalogu projektu i zawierał treść artykułu wraz z sugerowanymi miejscami na obrazy, jak również odpowiednio ustrukturyzowane nagłówki i akapity.

## Uwagi
- Upewnij się, że klucz API OpenAI jest usunięty lub zastąpiony przez `'YOUR_API_KEY'` przed udostępnieniem kodu.
- Wygenerowany HTML zawiera jedynie znaczniki `<body>`, bez dodatkowych sekcji HTML, CSS, lub JavaScript, zgodnie z wymaganiami zadania.

