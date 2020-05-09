import pytest
from hypothesis import given
from hypothesis.strategies import text
from pytest import approx

from squiggle import transform


@given(text(alphabet="ATGC"))
def test_end_x_value(s):
    transformed = transform(s, method="yau-bp")
    assert transformed[0][-1] == approx(
        s.count("A") + s.count("T") + s.count("G") + s.count("C")
    )


@given(text(alphabet="ATGC"))
def test_end_y_value(s):
    assert transform(s, method="yau-bp")[1][-1] == approx(
        s.count("T") - s.count("A") + 0.5 * (s.count("C") - s.count("G"))
    )


@given(text(alphabet="ATGC"))
def test_length(s):
    transformed = transform(s, method="yau-bp")
    assert (
        len(transformed[0]) == len(transformed[1]) == len(s) + 1
    )  # the extra 1 is for the starting (0, 0) coord


def test_basic():
    assert transform("ATGC", method="yau-bp") == ([0, 1, 2, 3, 4], [0, -1, 0, -0.5, 0])


def test_invalid():
    with pytest.raises(ValueError):
        transform("invalid", method="yau-bp")
