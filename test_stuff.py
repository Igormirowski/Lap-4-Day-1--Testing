import pytest
import stuff
import sys
from unittest import mock
import requests

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

# TEST 3  Num of sweets Error

def test_how_many_sweets():
    with pytest.raises(stuff.StuffError, match="We need some people to share sweets with!"):
        stuff.how_many_sweets(['sweet1','sweet2'], [])


# TEST 4 in terminal  greeting
def test_greeting(capsys):
    stuff.greeting("Beth")

    out, err = capsys.readouterr()
    sys.stdout.write(out)

    assert 'Beth' in out 
    assert out == "Hello, Beth!\n"

# TEST 5 cats
def test_find_cat_by_id(monkeypatch):
    mock_cats = [{'id': 1, 'name': 'Garfield'}, {'id': 2, 'name': "Happy"}]

    monkeypatch.setattr(stuff, 'cats', mock_cats)
    result = stuff.find_cat_by_id(2)
    assert result['name'] == 'Happy'
    # monkeypatch.setattr(obj, name, value, raising=True)

# TEST 5 API

def test_fetch_stuff():
    mock_respone = mock.Mock() #mock respone
    mock_respone.json.return_value = {
        "email": "test@example", "login": "testing"
    }
    mock_get = mock.Mock(return_value=mock_respone)
    requests.get = mock_get
    mock_get.assert_called_with("https://api.github.com/users/getfutureproof")
