"""Tests für textutils.word_count."""

from __future__ import annotations

from textutils import word_count


def test_empty_string_has_zero_words() -> None:
    assert word_count("") == 0


def test_whitespace_only_has_zero_words() -> None:
    assert word_count("   ") == 0


def test_multiple_and_edge_whitespace_are_not_counted() -> None:
    assert word_count("  a  b\n c ") == 3


def test_single_word_counts_once() -> None:
    assert word_count("ein") == 1


def test_tabs_and_newlines_split_words() -> None:
    assert word_count("\tfoo\nbar\r\nbaz\t") == 3
