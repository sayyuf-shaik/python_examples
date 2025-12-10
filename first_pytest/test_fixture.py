import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 15
    c = 20
    return [a, b, c]

@pytest.mark.skip
def test_method1(numbers):
    x = 10

    assert numbers[0] == x

def test_method2(numbers):
    y = 15

    assert numbers[1] == y


@pytest.mark.xfail
def test_method3(numbers):
    z = 8
    assert numbers[2] == z



