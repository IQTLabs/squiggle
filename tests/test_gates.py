import pytest
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

def test_A():
    assert transform("A", method="gates") == transform("a", method="gates") == ([0, 0], [0, -1])

def test_T():
    assert transform("T", method="gates") == transform("t", method="gates") == ([0, 0], [0, 1])

def test_G():
    assert transform("G", method="gates") == transform("g", method="gates") == ([0, 1], [0, 0])

def test_C():
    assert transform("C", method="gates") == transform("c", method="gates") == ([0, -1], [0, 0])

@given(text(alphabet="ATGC"))
def test_endpoint(s):
    # "If the function n(Z) denotes the number of occurrences of nucleotide Z
    # in a given sequence, the end-point of the sequence lies at coordinate
    # position [(n(G) - n(C)), (n(T) - n(A))]" (Gates, J. theor. Biol. 1986)
    transformed = transform(s, method="gates")
    assert transformed[0][-1] == s.count("G") - s.count("C")
    assert transformed[1][-1] == s.count("T") - s.count("A")
