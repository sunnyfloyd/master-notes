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

## Fixtures

-  `--setup-show` shows the order of operations of tests and fixtures, including the setup and teardown phases of the fixtures

- Fixtures are identified by their name - parameters that match names with a fixture are replaced with fixture's output. We never call fixture functions directly. pytest does that for us.

```python
@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

- Fixture functions run before the tests that use them. If there is a `yield` in the function, it stops there, passes control to the tests, and picks up on the next line after the tests are done. The code above the `yield` is “setup” and the code after `yield` is “teardown.” The code after the `yield`, the teardown, is guaranteed to run regardless of what happens during the tests. In our example, the `yield` happens within a context manager `with` block for the temporary directory. That directory stays around while the fixture is in use and the tests run. After the test is done, control passes back to the fixture, the `db.close()` can run, and then the `with` block can complete and clean up the directory.

```python
@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

def test_empty(cards_db):
    assert cards_db.count() == 0
```

### Fixture Scope

- The fixture decorator `scope` parameter allows to define a specific scope for a fixture:

    - `scope='function'`

    Run once per test function. The setup portion is run before each test using the fixture. The teardown portion is run after each test using the fixture. This is the default scope used when no scope parameter is specified.

    - `scope='class'` - run once per test class, regardless of how many test methods are in the class.

    - `scope='module'` - run once per module, regardless of how many test functions or methods or other fixtures in the module use it.

    - `scope='package'` - run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it.

    - `scope='session'` - run once per session. All test methods and functions using a fixture of session scope share one setup and teardown call.

- You can put fixtures into individual test files, but to share fixtures among multiple test files, you need to use a `conftest.py` file either in the same directory as the test file that’s using it or in some parent directory. The `conftest.py` file is also optional. It is considered by pytest as a “local plugin” and can contain hook functions and fixtures.

- To find available fixtures use `--fixtures` flag from given directory. You can also use `--fixtures-per-test` to see what fixtures are used by each test and where the fixtures are defined.

### Dynamic Fixture Scope

- Let’s say we have the fixture setup as we do now, with db at session scope and `cards_db` at function scope, but we’re worried about it. The `cards_db` fixture is empty because it calls `delete_all()`. If we don’t completely trust that `delete_all()` function yet, and want to put in place some way to completely set up the database for each test function we can do this by dynamically deciding the scope of the db fixture at runtime:

```python
def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test",
    )

def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"

@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()
```
