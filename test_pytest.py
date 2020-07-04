import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failed():
    assert (1, 2, 3) == (3, 2, 1)


"pytest -v -m my_mark"
@pytest.mark.smoke
@pytest.mark.my_mark
def test_my_mark():
    text = 'Test'
    assert len(text) == 4


@pytest.mark.xfail(reason='must be four')
def test_mark():
    text = 'Test'
    assert len(text) == 5


@pytest.mark.skipif(10 > 1, reason='Because 10 > 1')
def test_mark_2():
    text = 'Test'
    assert len(text) == 5


def test_mark_k_test():
    text = 'Test'
    assert len(text) == 4
