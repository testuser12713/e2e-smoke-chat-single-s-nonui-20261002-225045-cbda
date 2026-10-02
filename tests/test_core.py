"""Interface-Smoke-Test des Paketgerüsts.

Prüft ausschließlich Import, ``__all__`` und ``__version__`` des Pakets.
Die Randfall-Tests der einzelnen Funktionen liegen bei den jeweiligen
Feature-Tickets in ihren eigenen Testdateien.
"""

from __future__ import annotations

import importlib


def test_public_api_importable() -> None:
    from textutils import (
        is_palindrome,
        reverse_words,
        slugify,
        truncate,
        word_count,
    )

    assert callable(slugify)
    assert callable(truncate)
    assert callable(word_count)
    assert callable(is_palindrome)
    assert callable(reverse_words)


def test_all_contains_exactly_the_five_names_in_order() -> None:
    import textutils

    assert textutils.__all__ == [
        "slugify",
        "truncate",
        "word_count",
        "is_palindrome",
        "reverse_words",
    ]


def test_version() -> None:
    import textutils

    assert textutils.__version__ == "0.1.0"


def test_each_module_importable() -> None:
    for module_name in (
        "textutils.slugify",
        "textutils.truncate",
        "textutils.word_count",
        "textutils.palindrome",
        "textutils.reverse_words",
    ):
        assert importlib.import_module(module_name) is not None
