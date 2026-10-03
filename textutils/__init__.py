"""textutils — fünf unabhängige String-Hilfsfunktionen.

Öffentliche API: slugify, truncate, word_count, is_palindrome, reverse_words.
"""

from __future__ import annotations

from textutils.normalize_whitespace import normalize_whitespace
from textutils.palindrome import is_palindrome
from textutils.reverse_words import reverse_words
from textutils.slugify import slugify
from textutils.truncate import truncate
from textutils.word_count import word_count

# The sprint contract fixes this exact (non-alphabetical) order, so RUF022's
# alphabetical sort is deliberately not applied here.
__all__ = [  # noqa: RUF022
    "slugify",
    "truncate",
    "word_count",
    "is_palindrome",
    "reverse_words",
    "normalize_whitespace",
]

__version__ = "0.1.0"
