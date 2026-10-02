"""Tests für textutils.reverse_words."""

from __future__ import annotations

from textutils import reverse_words


def test_reverse_words_two_words() -> None:
    assert reverse_words("hello world") == "world hello"


def test_reverse_words_normalizes_spacing() -> None:
    assert reverse_words("  a  b ") == "b a"


def test_reverse_words_empty_string() -> None:
    assert reverse_words("") == ""


def test_reverse_words_single_word() -> None:
    assert reverse_words("ein") == "ein"


def test_reverse_words_only_whitespace() -> None:
    assert reverse_words("   ") == ""


def test_reverse_words_tabs_and_newlines() -> None:
    assert reverse_words("a\tb\nc") == "c b a"
