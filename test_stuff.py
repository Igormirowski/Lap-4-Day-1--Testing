import pytest

def do_maths(x, y):
    return x +y


# we check when operation happens we get expected
@pytest.mark.parametrize()
def test_do_maths(x, y, expected):
    assert do_maths(x,y) == expected

