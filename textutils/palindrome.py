"""Palindrome-Funktion: prüfen, ob ein Text ein Palindrom ist."""

from __future__ import annotations


def is_palindrome(text: str) -> bool:
    """Prüft, ob *text* ein Palindrom ist.

    Der Vergleich ignoriert Groß-/Kleinschreibung sowie alle nicht-
    alphanumerischen Zeichen. Leerer Text gilt als Palindrom.
    """
    normalized = [char.lower() for char in text if char.isalnum()]
    return normalized == normalized[::-1]
