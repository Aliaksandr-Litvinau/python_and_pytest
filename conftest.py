import pytest


@pytest.fixture(scope='session')
def start():
    print('start fixture')
    yield 1
    print('end test')


"""
https://docs.pytest.org/en/2.9.1/example/simple.html
Basic patterns and examples
1. В нашем примере мы ожидаем опцию в командной строке --foo (функция pytest_addoption)
Например pytest --foo=bar
2. Для того, что бы 'вытащить' эту опцию, используем функцию get_option_foo
3. Для примера, смотрите тест test_ini.py::test_ini
"""


def pytest_addoption(parser):
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")


@pytest.fixture
def get_option_foo(request):
    return request.config.getoption("--foo")
