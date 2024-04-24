from katas.fill_square import fill_square
import pytest


def test_only_accepts_list_of_lists():
    values = [['a'], ['a', []]]
    for value in values:
        with pytest.raises(ValueError) as v:
            fill_square(value)
        assert str(v.value) == 'List of lists only!'


def test_returns_simple_list():
    invoke = fill_square([[1]])
    assert invoke == [[1]]


def test_fills_empty_single_list():
    invoke = fill_square([[]])
    assert invoke == [[None]]


def test_fills_empty_simple_list():
    invoke = fill_square([[1], []])
    assert invoke == [[1], [None]]


def test_creates_new_lists_filled_with_None():
    invoke = fill_square([[1, 2]])
    assert invoke == [[1, 2], [None, None]]


def test_completes_the_square():
    invoke = fill_square([[1, 2], [3, 2, 1], [1]])
    assert invoke == [[1, 2, None], [3, 2, 1], [1, None, None]]
