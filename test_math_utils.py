from math_utils import MathUtils

def test_add():
    assert MathUtils.add(2, 3) == 5
    assert MathUtils.add(-2, -3) == -5

def test_subtract():
    assert MathUtils.subtract(5, 3) == 2
    assert MathUtils.subtract(3, 5) == -2

def test_multiply():
    assert MathUtils.multiply(4, 3) == 12
    assert MathUtils.multiply(0, 5) == 0

def test_divide():
    assert MathUtils.divide(10, 2) == 5.0
    assert MathUtils.divide(5, 0) == -1.0
