import pytest

@pytest.mark.one
def test_method1():
    a = 15
    b = 20
    assert 5 + a == b

@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + b == 20


