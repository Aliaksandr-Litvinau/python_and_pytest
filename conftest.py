import pytest


@pytest.fixture(scope='session')
def start():
    print('start fixture')
    yield 1
    print('end test')


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo
