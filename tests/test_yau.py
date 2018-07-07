import pytest
from pytest import approx
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

def test_A():
    assert transform("A", method="yau") == transform("a", method="yau") == ([0, 0.5], [0, -(3**0.5) / 2])

def test_T():
    assert transform("T", method="yau") == transform("t", method="yau") == ([0, 0.5], [0, (3**0.5) / 2])

def test_G():
    assert transform("G", method="yau") == transform("g", method="yau") == ([0, (3**0.5) / 2], [0, -0.5])

def test_C():
    assert transform("C", method="yau") == transform("c", method="yau") == ([0, (3**0.5) / 2], [0, 0.5])

@given(text(alphabet="ATGC"))
def test_end_x_value(s):
    assert transform(s, method="yau")[0][-1] == approx(((3**0.5) / 2 * (s.count("C") + s.count("G"))) + (0.5 * (s.count("A") + s.count("T"))))

@given(text(alphabet="ATGC"))
def test_end_y_value(s):
    assert transform(s, method="yau")[1][-1] == approx((-(3**0.5) / 2 * s.count("A")) + ((3**0.5) / 2 * s.count("T")) + (0.5 * s.count("C")) + (-0.5 * s.count("G")))
