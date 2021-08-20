import random

import pytest
import os

directory = 'test_dir'


# @pytest.fixture()
# def create_dir():
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#
# def test_create_dir(create_dir):
#     assert os.path.exists(directory), 'dir not exist'


@pytest.fixture(scope="session")
def get_random_number():
    number = random.randint(1, 100)
    print(number)
    return number


def test_random_number(get_random_number):
    assert 0 < get_random_number <= 100


def test_random_number_2(get_random_number):
    assert 0 < get_random_number <= 100


class TestRandom:
    def test_random_number_1(self, get_random_number):
        assert 0 < get_random_number <= 100

    def test_random_number_2(self, get_random_number):
        assert 0 < get_random_number <= 100
