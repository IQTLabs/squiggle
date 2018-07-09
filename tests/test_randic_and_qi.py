import pytest
from hypothesis import given
from hypothesis.strategies import text

from squiggle import transform

randic = dict(A=3, T=2, G=1, C=0)
qi = {'AA': 12,
      'AC': 4,
      'GT': 6,
      'AG': 0,
      'CC': 13,
      'CA': 5,
      'CG': 10,
      'TT': 15,
      'GG': 14,
      'GC': 11,
      'AT': 8,
      'GA': 1,
      'TG': 7,
      'TA': 9,
      'TC': 3,
      'CT': 2}

@given(text(alphabet="ATGC"))
def test_randic(s):
    transformed = transform(s, method="randic")
    for i, letter in enumerate(s):
        assert transformed[1][i] == randic[letter]

@given(text(alphabet="ATGC", min_size=2))
def test_qi(s):

    transformed = transform(s, method="qi")
    for i in range(len(s)):
        try:
            assert transformed[1][i] == qi[s[i:i + 2]]
        except IndexError:
            pass

def test_bad_seq():
    with pytest.raises(ValueError):
        transform("INVALID", method="randic")
    with pytest.raises(ValueError):
        transform("INVALID", method="qi")
