"""Normalize-Whitespace-Funktion: Whitespace eines Textes vereinheitlichen."""

from __future__ import annotations


def normalize_whitespace(text: str) -> str:
    """Normalisiert den Whitespace in *text* zu einzelnen Leerzeichen."""
    return " ".join(text.split())
