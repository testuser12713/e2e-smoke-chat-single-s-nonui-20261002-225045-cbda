"""Tests für textutils.palindrome.is_palindrome."""

from __future__ import annotations

from textutils.palindrome import is_palindrome


def test_empty_string_is_palindrome() -> None:
    assert is_palindrome("") is True


def test_non_alphanumeric_only_is_palindrome() -> None:
    assert is_palindrome("!!!") is True


def test_non_palindrome_returns_false() -> None:
    assert is_palindrome("abc") is False


def test_case_insensitive_palindrome() -> None:
    assert is_palindrome("Anna") is True


def test_sentence_with_punctuation_is_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_german_palindrome() -> None:
    assert is_palindrome("Lagerregal") is True
