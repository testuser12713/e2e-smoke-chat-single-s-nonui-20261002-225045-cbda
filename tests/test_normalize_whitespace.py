"""Tests für textutils.normalize_whitespace."""

from __future__ import annotations

from textutils import normalize_whitespace


def test_multiple_spaces_collapse_to_one() -> None:
    assert normalize_whitespace("  foo   bar   baz  ") == "foo bar baz"


def test_tab_and_newline_become_single_space() -> None:
    assert normalize_whitespace("foo\tbar\nbaz") == "foo bar baz"


def test_leading_and_trailing_whitespace_removed() -> None:
    assert normalize_whitespace("  foo bar \t baz\n") == "foo bar baz"


def test_empty_string() -> None:
    assert normalize_whitespace("") == ""


def test_only_whitespace() -> None:
    assert normalize_whitespace("   \t\n  ") == ""


def test_already_normalized_unchanged() -> None:
    assert normalize_whitespace("foo bar") == "foo bar"


def test_unicode_non_breaking_space() -> None:
    assert normalize_whitespace("foo\u00a0bar") == "foo bar"
