"""Tests für textutils.slugify."""

from __future__ import annotations

import pytest

from textutils.slugify import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hallo Welt!", "hallo-welt"),
        ("  Mehr---fach   Trenner ", "mehr-fach-trenner"),
        ("", ""),
        ("...", ""),
        ("Crème brûlée", "creme-brulee"),
        ("Müller", "muller"),
    ],
)
def test_slugify(text: str, expected: str) -> None:
    assert slugify(text) == expected
