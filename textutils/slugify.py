"""Slugify-Funktion: Text in einen URL-tauglichen Slug umwandeln."""

from __future__ import annotations

import re
import unicodedata

_SEPARATOR_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Wandelt *text* in einen kleingeschriebenen, trenner-normalisierten Slug um.

    Akzente werden auf ihre ASCII-Grundform reduziert, nicht-alphanumerische
    Zeichen werden durch einen einzelnen Bindestrich ersetzt und führende bzw.
    abschließende Trennzeichen entfernt.
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = _SEPARATOR_RE.sub("-", ascii_text.lower())
    return slug.strip("-")
