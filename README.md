# textutils

`textutils` ist eine eigenständige, installierbare Python-Bibliothek ohne UI. Sie
bündelt sechs kleine, voneinander unabhängige String-Hilfsfunktionen
(`slugify`, `truncate`, `word_count`, `is_palindrome`, `reverse_words`,
`normalize_whitespace`) in einem Paket. Es gibt keine CLI und keine Services.

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
from textutils import (
    is_palindrome,
    normalize_whitespace,
    reverse_words,
    slugify,
    truncate,
    word_count,
)
```

Die Bibliothek benötigt keine Konfiguration und keine Umgebungsvariablen.

## Funktionen

- `slugify(text: str) -> str` — URL-tauglicher Slug, Akzente reduziert.
- `truncate(text: str, max_len: int) -> str` — Kürzung auf `max_len` Zeichen mit Ellipse `…`.
- `word_count(text: str) -> int` — Anzahl der Wörter.
- `is_palindrome(text: str) -> bool` — Palindrom-Prüfung über alphanumerischen Vergleich.
- `reverse_words(text: str) -> str` — Umkehr der Wortreihenfolge.
- `normalize_whitespace(text: str) -> str` — Vereinheitlichung des Whitespace zu einzelnen Leerzeichen.
