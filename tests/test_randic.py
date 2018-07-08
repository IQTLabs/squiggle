import pytest
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

heights = dict(A=3, T=2, G=1, C=0)

@given(text(alphabet="ATGC"))
def test_randic(s):
    transformed = transform(s, method="randic")
    for i, letter in enumerate(s):
        assert transformed[1][i] == heights[letter]
