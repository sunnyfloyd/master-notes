# Pytest

## Short Intro

- to run specific tests use `pytest test_path.py::TestClassName::test_method`

- to run tests matching given name pattern `pytest -k pattern`: `pytest -v --tb=no -k "(dict or ids) and not TestEquality"`. Allowed patterns include keywords: `and/or/not/parentheses`.

- use `pytest -v` for verbose test output

- use `pytest -vv` for more information during test failures

- files with tests and test functions need to start with `test_`

- `parametrize` in pytest:

```python
import pytest

from blackjack import card_score

@pytest.mark.parametrize("cards,score", [('JK', 20), ('KKK', 0), ('AA', 12), ('AK', 21)])
def test_simple_usecase(cards, score):
    assert card_score(cards) == score
```

- coverage report can be produced with `pytest --cov blackjack --cov-report html` after installing `pytest-cov` package

- `pytest --tb=short` - shortens traceback for failing tests with raised exceptions

- using pytest for each commit on GitHub and GitLab automatically

```yaml
# .github/workflows/pythonpackage.yml
name: Python package

on: [push, pull_request]

jobs:
build:
  runs-on: ubuntu-latest
  strategy:
  matrix:
      python-version: [3.7]

  steps:
  - uses: actions/checkout@v2
  - name: Set up Python ${{ matrix.python-version }}
  uses: actions/setup-python@v1
  with:
      python-version: ${{ matrix.python-version }}
  - name: Test with pytest
  run: |
      pip install pytest
      pytest --verbose
```

## Structuring Test Functions

- Use **Act-Arrange-Assert** or **Given-When-Then** test approach:

  1. **Given/Arrange** — A starting state. This is where you set up data or the environment to get ready for the action.
  2. **When/Act** — Some action is performed. This is the focus of the test—the behavior we are trying to make sure is working right.
  3. **Then/Assert** — Some expected result or end state should happen. At the end of the test, we make sure the action resulted in the expected behavior.

## Assertion Helper Function

- An **assertion helper** is a function that is used to wrap up a complicated assertion check.

```python
​from​ ​cards​ ​import​ Card
​import​ ​pytest​
​
    def ​assert_identical​(c1: Card, c2: Card):
        __tracebackhide__ = True
        ​assert​ c1 == c2
        ​if​ c1.id != c2.id:
        pytest.fail(f​"id's don't match. {c1.id} != {c2.id}"​)
​
​
​ 	​def​ ​test_identical​():
        c1 = Card(​"foo"​, id=123)
        c2 = Card(​"foo"​, id=123)
        assert_identical(c1, c2)
​
​
​ 	​def​ ​test_identical_fail​():
        c1 = Card(​"foo"​, id=123)
        c2 = Card(​"foo"​, id=456)
        assert_identical(c1, c2)
```

-  The `assert_identical` function sets` __tracebackhide__ = True`. This is optional. The effect will be that failing tests will not include this function in the traceback. The normal `assert c1 == c2` is then used to check everything except the ID for equality. Finally, the IDs are checked, and if they are not equal, `pytest.fail()` is used to fail the test with a hopefully helpful message.


## Testing for Expected Exceptions

- testing for raised exceptions:

```python
import pytest

from blackjack.common import card_score

def test_raise_error():
    with pytest.raises(ValueError):
        card_score("")
```

- We can also check to make sure the message is correct, or any other aspect of the exception, like additional parameters:

```python
​def​ ​test_raises_with_info​():
    match_regex = ​"missing 1 .* positional argument"​
    ​with​ pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()
​
​
​def​ ​test_raises_with_info_alt​():
    ​with​ pytest.raises(TypeError) ​as​ exc_info:
        cards.CardsDB()
    expected = ​"missing 1 required positional argument"​
    ​assert​ expected ​in​ str(exc_info.value)
```

- The match parameter takes a regular expression and matches it with the exception message. You can also use as `exc_info` or any other variable name to interrogate extra parameters to the exception if it’s a custom exception. The `exc_info` object will be of type `ExceptionInfo`.
