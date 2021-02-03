import pytest


def test_a():
    print("test_demo       test_a")


def test_b():
    print("test_demo       test_b")


def test_c():
    assert 1 == 2


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [3, 4, 5])
def test_param(a, b):
    print(f"a = {a},b = {b}")
