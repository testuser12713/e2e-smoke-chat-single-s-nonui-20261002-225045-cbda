"""Truncate-Funktion: Text auf eine maximale Länge kürzen."""

from __future__ import annotations


def truncate(text: str, max_len: int) -> str:
    """Kürzt *text* auf höchstens *max_len* Zeichen.

    Überschreitet der Text die Grenze, wird er mit einem Ellipsenzeichen '…'
    abgeschlossen, das in die Länge von *max_len* eingerechnet wird.
    """
    raise NotImplementedError
