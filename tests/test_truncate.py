"""Tests für textutils.truncate.truncate."""

from __future__ import annotations

import pytest

from textutils import truncate


def test_truncate_hello_world_at_five() -> None:
    assert truncate("hello world", 5) == "hell…"


def test_truncate_abc_at_one_is_just_ellipsis() -> None:
    assert truncate("abc", 1) == "…"


def test_truncate_abc_at_zero_is_empty() -> None:
    assert truncate("abc", 0) == ""


def test_truncate_abc_at_negative_is_empty() -> None:
    assert truncate("abc", -3) == ""


def test_truncate_text_that_fits_is_unchanged() -> None:
    assert truncate("hello", 10) == "hello"


@pytest.mark.parametrize("max_len", [0, 1, 2, 3, 5, 10, 50, 100])
def test_truncate_never_exceeds_max_len(max_len: int) -> None:
    text = "hello world"
    result = truncate(text, max_len)
    assert len(result) <= max_len
    if max_len >= 1 and len(text) > max_len:
        assert result.endswith("…")
    elif len(text) <= max_len:
        assert result == text
