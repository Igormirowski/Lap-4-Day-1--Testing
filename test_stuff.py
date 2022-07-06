import pytest
import stuff



# TEST 1 
# we check when operation happens we get expected

@pytest.mark.parametrize('x, y, expected', [(2, 4, 6),(3, 4, 7), (9, 2, 11)]) # values replace values from line 3 
def test_do_maths(x, y, expected):
    assert stuff.do_maths(x,y) == expected


# TEST 2
