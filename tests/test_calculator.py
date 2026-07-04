import pytest
from calculator import add, subtract, multiply, divide, get_history, clear_history


@pytest.fixture(autouse=True)
def reset_history():
    clear_history()
    yield
    clear_history()


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_invalid_input():
    with pytest.raises(TypeError, match="a must be a real number"):
        add("2", 3)


def test_history():
    add(1, 2)
    divide(8, 4)
    assert get_history() == [
        "add(1, 2) = 3",
        "divide(8, 4) = 2.0",
    ]
