# Lap 4 Day 1 Testing 

- `pipenv shell`
- `pipenv install --dev pytest`
- `pytest .` see no test
### Test: 
    - 2 + 2
    - add element to array
    - test errors
    - look for thing in terminal (test for terminal)
    - mocking
- Unrecognized pytest FIX:
    - Check name of your virtual environment `pipenv --venv` / `pipenv --where`
    - COMMAND + Shift + P : > reload windown
    - COMMAND + Shift + P (interpreter pick from link venv(vid22))

- `import pytest` to test file
- create tests 
```
@pytest.mark.parametrize('x,y,expected', [(2, 4, 6),(3, 4, 7), (9, 2, 11)])
def test_do_maths(x, y, expected):
    assert do_maths(x,y) == expected
```
- `pytest .`
- `import stuff` + (add `stuff.do_maths` to test) function will be in file not test file!

## More
- NOT TYPE `pytest .`
add scripts to pipfile and run: `pipenv run test`
```
[scripts]
test = "pytest ."
```

- install: `pipenv install --dev pytest-cov`
- add in pipfile scripts
```
coverage = "pytest --cov-report term-missing --cov-."
```

- `pipenv run coverage` Coverage
- add more functions (add_fruits) and test
- we implement fixture 

