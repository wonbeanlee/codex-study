import pytest

from calculator import add, substract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-2, 3, 1), (0.1, 0.2, 0.3)])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (3, 5, -2), (-2, -3, 1)])
def test_substract(a, b, expected):
    assert substract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-2, 3, -6), (5, 0, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (5, 2, 2.5), (-6, 3, -2), (0, 3, 0)])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [(5, 0), (0, 0), (-5, 0.0)])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError):
        divide(a, b)
