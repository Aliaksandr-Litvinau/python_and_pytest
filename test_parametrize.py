import pytest


# @pytest.mark.parametrize('value_1, value_2, result', (
#     (1, 2, 3),
#     (2, 5, 7),
#     (100, 200, 301)
#                          ))
# def test_sum(value_1, value_2, result):
#     assert value_1 + value_2 == result, "Результат сложения не совпадает"

@pytest.mark.parametrize('value1, value2, result', [
    [1, 2, 3],
    [10, 20, 30],
    [-1, 1, 10]
])
def test_sum(value1, value2, result):
    assert value1 + value2 == result, "Результат сложения не совпадает"
