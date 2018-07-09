import pytest
from pytest import approx
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

@given(text(alphabet="ATGC"))
def test_end_x_value(s):
    transformed = transform(s, method="yau-bp")
    assert transformed[0][-1] == approx(s.count("A") + s.count("T") + s.count("G") + s.count("C"))

@given(text(alphabet="ATGC"))
def test_end_y_value(s):
    assert transform(s, method="yau-bp")[1][-1] == approx(s.count("T") - s.count("A") + 0.5 * (s.count("C") - s.count("G")))
