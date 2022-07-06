import pytest
import stuff

# TEST 1 
# we check when operation happens we get expected

@pytest.mark.parametrize('x, y, expected', [(2, 4, 6),(3, 4, 7), (9, 2, 11)]) # values replace values from line 3 
def test_do_maths(x, y, expected):
    assert stuff.do_maths(x,y) == expected



@pytest.fixture
def fruits_test_data():
    return ["banana", "pear"]

# TEST 2  add to array function 
def test_add_fruit(fruits_test_data):
    salad = stuff.add_fruit('mango', fruits_test_data)
    assert 'mango' in salad
    # element is in the array

# TEST 3  Errors
