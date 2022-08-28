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

- `-s` flag is a shortcut flag for `--capture=no` that **tells pytest to turn off output capture**. I used it because the new fixtures have print functions in them, and I wanted to see the output. **Without turning off output capture, pytest only prints the output of tests that fail**.

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

-  `--setup-show` shows the order of operations of tests and fixtures, including the setup and teardown phases of the fixtures.

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

- It is possible to rename fixtures using `name` parameter:

```python
@pytest.fixture(name=​"ultimate_answer"​)
​def​ ​ultimate_answer_fixture​():
    ​return​ 42
```

### Fixture Scope

- The fixture decorator `scope` parameter allows to define a specific scope for a fixture:

    - `scope='function'`

    Run once per test function. The setup portion is run before each test using the fixture. The teardown portion is run after each test using the fixture. This is the default scope used when no scope parameter is specified.

    - `scope='class'` - run once per test class, regardless of how many test methods are in the class.

    - `scope='module'` - run once per module, regardless of how many test functions or methods or other fixtures in the module use it.

    - `scope='package'` - run once per package, or test directory, regardless of how many test functions or methods or other fixtures in the package use it.

    - `scope='session'` - run once per session. All test methods and functions using a fixture of session scope share one setup and teardown call.

- You can put fixtures into individual test files, but to share fixtures among multiple test files, you need to place them in a `conftest.py` file either in the same directory as the test file that’s using it or in some parent directory. The `conftest.py` file is also optional. It is considered by pytest as a “local plugin” and can contain hook functions and fixtures.

- To find available fixtures use `--fixtures` flag from given directory. You can also use `--fixtures-per-test` to see what fixtures are used by each test and where the fixtures are defined.

### Dynamic Fixture Scope

- Let’s say we have the fixture setup as we do now, with db at session scope and `cards_db` at function scope, but we’re worried about it. The `cards_db` fixture is empty because it calls `delete_all()`. If we don’t completely trust that `delete_all()` function yet, and want to put in place some way to completely set up the database for each test function we can do this by dynamically deciding the scope of the db fixture at runtime. Additionally, we depend on a new command-line flag,` --func-db`. In order to allow pytest to allow us to use this new flag, we need to write a hook function `pytest_adoption`:

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

### autouse for Fixtures That Are Always Used

- You can use `autouse=True` to get a fixture to run all of the time. This works well for code you want to run at certain times, but tests don’t really depend on any system state or data from the fixture:

```python
import​ ​pytest​
​import​ ​time​

@pytest.fixture(autouse=True)
​def​ ​footer_function_scope​():
    ​"""Report test durations after each function."""​
    start = time.time()
    ​yield​
    stop = time.time()
    delta = stop - start
    ​print​(​"​​\n​​test duration : {:0.3} seconds"​.format(delta))
```

### Builtin Fixtures

#### tmp_path and tmp_path_factory

- The `tmp_path` and `tmp_path_factory` fixtures are used to create temporary directories. The `tmp_path` function-scope fixture returns a `pathlib.Path` instance that points to a temporary directory that sticks around during your test and a bit longer. The `tmp_path_factory` session-scope fixture returns a `TempPathFactory` object. This object has a `mktemp()` function that returns `Path` objects. You can use `mktemp()` to create multiple temporary directories. 

```python
​def​ ​test_tmp_path​(tmp_path):
    file = tmp_path / ​"file.txt"​
    file.write_text(​"Hello"​)
    ​assert​ file.read_text() == ​"Hello"​
 	
 	
​def​ ​test_tmp_path_factory​(tmp_path_factory):
    path = tmp_path_factory.mktemp(​"sub"​)
    file = path / ​"file.txt"​
    file.write_text(​"Hello"​)
    ​assert​ file.read_text() == ​"Hello"​
```

#### capsys

- The `capsys` fixture enables the capturing of writes to stdout and stderr.

```python
​import​ ​cards​
​
​​def​ ​test_version_v2​(capsys):
​   cards.cli.version()
    output = capsys.readouterr().out.rstrip()
​   ​assert​ output == cards.__version__
```

#### monkeypatch

- The monkeypatch fixture provides the following functions:

    - `setattr(target, name, value, raising=True)` — Sets an attribute
    - `delattr(target, name, raising=True)` — Deletes an attribute
    - `setitem(dic, name, value)` — Sets a dictionary entry
    - `delitem(dic, name, raising=True)` — Deletes a dictionary entry
    - `setenv(name, value, prepend=None)` — Sets an environment variable
    - `delenv(name, raising=True)` — Deletes an environment variable
    - `syspath_prepend(path)` — Prepends path to `sys.path`, which is Python’s list of import locations
    - `chdir(path)` — Changes the current working directory

- The `raising` parameter tells pytest whether or not to raise an exception if the item doesn’t already exist. The prepend parameter to `setenv()` can be a character. If it is set, the value of the environment variable will be changed to `value + prepend + <old value>`.

- We can use `monkeypatch` to redirect the CLI to a temporary directory for the database in a couple of ways. Both methods involve knowledge of the application code:

```python
# original method
​def​ ​get_path​():
    db_path_env = os.getenv(​"CARDS_DB_DIR"​, ​""​)
    ​if​ db_path_env:
        db_path = pathlib.Path(db_path_env)
    ​else​:
        db_path = pathlib.Path.home() / ​"cards_db"​
    ​return​ db_path

# 1st method (patching the entire get_path function)
​def​ ​test_patch_get_path​(monkeypatch, tmp_path):
    ​def​ ​fake_get_path​():
        ​return​ tmp_path
​
    monkeypatch.setattr(cards.cli, ​"get_path"​, fake_get_path)
    ​assert​ run_cards(​"config"​) == str(tmp_path)

#2nd method (pathing environment variable)
def​ ​test_patch_env_var​(monkeypatch, tmp_path):
    monkeypatch.setenv(​"CARDS_DB_DIR"​, str(tmp_path))
    ​assert​ run_cards(​"config"​) == str(tmp_path)
```

## Parametrization

- Parameters (their string representation to be more specifc) can be used to select only subset of test using `-k` flag, f.i.: `​​pytest​​ ​​-v​​ ​​-k​​ ​​todo​`.

### Parametrizing Functions

- To parametrize a test function, add parameters to the test definition and use the `@pytest.mark.parametrize()` decorator to define the sets of arguments to pass to the test:

```python
@pytest.mark.parametrize(
​   "start_summary, start_state"​,  # this can be either strign or a list
    [
        (​"write a book"​, ​"done"​),
        (​"second edition"​, ​"in prog"​),
        (​"create a course"​, ​"todo"​),
    ],
​)
​def​ ​test_finish​(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
​
    cards_db.finish(index)
​
    card = cards_db.get_card(index)
    ​assert​ card.state == ​"done"​
```

### Parametrizing Fixtures

- When using fixtures parametrization pytest will call the fixture once each for every set of values we provide. Then downstream, every test function that depends on the fixture will be called, once each for every fixture value:

```python
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
```

- Fixture parametrization has the benefit of having a fixture run for each set of arguments. This is useful if you have setup or teardown code that needs to run for each test case

### Parametrizing with pytest_generate_tests

- The third way to parametrize is by using a hook function called `pytest_generate_tests`.

```python
def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])


def test_finish(cards_db, start_state):0
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
```

- Parametrizing with hook function can be useful when:

    - We could base our parametrization list on a command-line flag, since `metafunc` gives us access to `metafunc.config.getoption`("`--someflag`"). Maybe we add a `--excessive` flag to test more values, or a `--quick` flag to test just a few.

    - The parametrization list of a parameter could be based on the presence of another parameter. For example, for test functions asking for two related parameters, we can parametrize them both with a different set of values than if the test is just asking for one of the parameters.

## Markers

- These are the most commonly used of the markers builtins:

    - `@pytest.mark.parametrize()`
    - `@pytest.mark.skip()`
    - `@pytest.mark.skipif()`
    - `@pytest.mark.xfail()`

- With both the `skip` and the `skipif` markers, the test is not actually run. If we want to run the test anyway, we can use `xfail`.

- To list all the markers available, including descriptions and parameters, run `pytest --markers`.

### pytest.mark.skip

- Can be used when feature is not yet completed.

- It makes sense to run such tests with `-ra` flag that includes short summary of tests with a reason of adding marker to them. `a` part of a flag means that all reasons will be listed apart from the passed ones.

```python
@pytest.mark.skip(reason="Card doesn't support < comparison yet")
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2
```

### pytest.mark.skipif

- The `skipif` marker allows you to pass in as many conditions as you want and if any of them are true, the test is skipped.

-  We might want to use `skipif` is if we have tests that need to be written differently on different operating systems. We can write separate tests for each OS and skip on the inappropriate OS.

```python
@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2

```

### pytest.mark.xfail

- If we want to run all tests, even those that we know will fail, we can use the `xfail` marker.

- For tests marked with `xfail`:

    - Failing tests will result in `XFAIL`.
    - Passing tests (with no strict setting) will result in `XPASSED`.
    - Passing tests with `strict=true` will result in `FAILED`.

```python
@pytest.mark.xfail(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


@pytest.mark.xfail(reason="XPASS demo")
def test_xpass():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


@pytest.mark.xfail(reason="strict demo", strict=True)
def test_xfail_strict():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
```

### Custom Markers

- Custom markers are markers we make up ourselves and apply to tests. Think of them like tags or labels. Custom markers can be used to select tests to run or skip. Convention is to use `smoke` marker to indicate crucial tests.

```python
@pytest.mark.smoke
def test_start(cards_db):
    """
    start changes state from "todo" to "in prog"
    """
    i = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"
```

- To run a specific subset of tests marked with a marker use `pytest -m mark_name` flag. We can also use additional logic in the flag like: `​​pytest​​ ​​-v​​ ​​-m​​ ​​"finish and exception"​`.

- It is recommended to use strict markers either by adding a flag to a command line `pytest​​ ​​--strict-markers​​ ​​-m​​ ​​smoke​` or just by adding it to the `pytest.ini`:

```ini
adopts =
    ​--strict-markers​
```

- To avoid pytest warning we need to register it in the `pytest.ini`:

```ini
markers =
    ​smoke:​ ​subset​ ​of​ ​tests​
    exception:​ ​check​ ​for​ ​expected​ ​exceptions​
```

#### Marking Files

- If pytest sees a `pytestmark` attribute in a test module, it will apply the marker(s) to all the tests in that module. If you want to apply more than one marker to the file, you can use a list form: `pytestmark = [pytest.mark.marker_one, pytest.mark.marker_two]`.

### Combining Markers with Fixtures

```python
@pytest.fixture(scope="function")
def cards_db(session_cards_db, request, faker):
    db = session_cards_db
    db.delete_all()

    # support for `@pytest.mark.num_cards(<some number>)`

    # random seed
    faker.seed_instance(101)
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(
                Card(summary=faker.sentence(), owner=faker.first_name())
            )
    return db

@pytest.mark.num_cards(3)
​def​ ​test_three_cards​(cards_db):
    ​assert​ cards_db.count() == 3
```

## Testing Strategy

- Prioritization of testing:

    - **Recent** — New features, new areas of code, new functionality that has been recently repaired, refactored, or otherwise modified

    - **Core** — Your product’s unique selling propositions (USPs). The essential functions that must continue to work in order for the product to be useful

    -**Risk** — Areas of the application that pose more risk, such as areas important to customers but not used regularly by the development team or parts that use third-party code you don’t quite trust

    - **Problematic** — Functionality that frequently breaks or often gets defect reports against it

    - **Expertise** — Features or algorithms understood by a limited subset of people

- When creating a test cases try to think about the following:

  1. Start with a non-trivial, “happy path” test case.

  2. Then look at test cases that represent
    - interesting sets of input,
    - interesting starting states,
    - interesting end states, or
    - all possible error states.
