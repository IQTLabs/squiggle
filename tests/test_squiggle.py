import pytest
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

def test_transform_A():
    assert transform("A") == transform("a") == ([0, 0.5, 1.0], [0, 1.0, 0])

def test_transform_T():
    assert transform("T") == transform("t") == ([0, 0.5, 1.0], [0, -1.0, -2.0])

def test_transform_G():
    assert transform("G") == transform("g") == ([0, 0.5, 1.0], [0, 1.0, 2.0])

def test_transform_C():
    assert transform("C") == transform("c") == ([0, 0.5, 1.0], [0, -1.0, 0])

def test_transform_multiple():
    assert transform("ATG") == ([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
                                [0, 1.0, 0, -1.0, -2.0, -1.0, 0.0])
    assert transform("TTC") == ([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
                                [0, -1.0, -2.0, -3.0, -4.0, -5.0, -4.0])
@given(text(alphabet="ATGC"))
def test_length(s):
    transformed = transform(s)
    assert len(transformed[0]) == len(transformed[1]) == 2 * len(s) + 1 # the extra 1 is for the starting (0, 0) coord
