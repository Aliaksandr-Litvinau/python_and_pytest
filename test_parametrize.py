import pytest


@pytest.mark.parametrize('value_1, value_2, result', [
    (1, 2, 3),
    (2, 5, 7),
    (100, 200, 301)
])
def test_sum(value_1, value_2, result):
    assert value_1 + value_2 == result, "Результат сложения не совпадает"

