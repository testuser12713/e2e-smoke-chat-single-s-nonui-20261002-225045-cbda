"""Slugify-Funktion: Text in einen URL-tauglichen Slug umwandeln."""

from __future__ import annotations


def slugify(text: str) -> str:
    """Wandelt *text* in einen kleingeschriebenen, trenner-normalisierten Slug um.

    Akzente werden auf ihre ASCII-Grundform reduziert, nicht-alphanumerische
    Zeichen werden durch einen einzelnen Bindestrich ersetzt und führende bzw.
    abschließende Trennzeichen entfernt.
    """
    raise NotImplementedError
