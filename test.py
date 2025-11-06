import pytest
from main import Polynomial


def test_addition():
    p1 = Polynomial()
    p2 = Polynomial()
    p1.add_term(2, 2)
    p1.add_term(3, 1)
    p2.add_term(1, 2)
    p2.add_term(4, 0)

    result = p1 + p2

    expected = Polynomial()
    expected.add_term(3, 2)
    expected.add_term(3, 1)
    expected.add_term(4, 0)

    assert result == expected


def test_multiplication():
    p1 = Polynomial()
    p2 = Polynomial()
    p1.add_term(1, 1)
    p1.add_term(1, 0)
    p2.add_term(1, 1)
    p2.add_term(-1, 0)

    result = p1 * p2

    expected = Polynomial()
    expected.add_term(1, 2)
    expected.add_term(-1, 1)
    expected.add_term(1, 1)
    expected.add_term(-1, 0)

    assert result == expected
