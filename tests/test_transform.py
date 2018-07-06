import pytest
from squiggle import transform

def test_transform_A():
    assert transform("A") == transform("a") == ([0, 0.5, 1.0], [0, 1.0, 0])

def test_transform_T():
    assert transform("T") == transform("t") == ([0, 0.5, 1.0], [0, -1.0, -2.0])

def test_transform_G():
    assert transform("G") == transform("g") == ([0, 0.5, 1.0], [0, 1.0, 2.0])

def test_transform_C():
    assert transform("C") == transform("c") == ([0, 0.5, 1.0], [0, -1.0, 0])
