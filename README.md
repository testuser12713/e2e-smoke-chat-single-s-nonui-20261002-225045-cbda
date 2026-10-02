# textutils

`textutils` ist eine eigenständige, installierbare Python-Bibliothek ohne UI. Sie
bündelt fünf kleine, voneinander unabhängige String-Hilfsfunktionen
(`slugify`, `truncate`, `word_count`, `is_palindrome`, `reverse_words`) in einem
Paket. Es gibt keine CLI, keine Services und keine Zusatzfeatures.

## Tech-Stack

- Python >= 3.9
- Nur Standardbibliothek, keine Laufzeit-Abhängigkeiten
- Tests mit pytest

## Installation

```console
pip install -e .
```

## Tests

```console
pytest
```

## Verwendung

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

Die Bibliothek benötigt keine Konfiguration und keine Umgebungsvariablen.

## Funktionen

- `slugify(text: str) -> str` — URL-tauglicher Slug, Akzente reduziert.
- `truncate(text: str, max_len: int) -> str` — Kürzung auf `max_len` Zeichen mit Ellipse `…`.
- `word_count(text: str) -> int` — Anzahl der Wörter.
- `is_palindrome(text: str) -> bool` — Palindrom-Prüfung über alphanumerischen Vergleich.
- `reverse_words(text: str) -> str` — Umkehr der Wortreihenfolge.
