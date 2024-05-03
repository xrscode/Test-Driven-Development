from katas.binary_score import score
import pytest


def test_only_accepts_list():
    values = ['a', None, False, True, {}, ()]
    for value in values:
        with pytest.raises(TypeError) as t:
            score(value)
        assert str(t.value) == 'List only!'


def test_list_contains_ints_only():
    values = ['a', None, False, True, {}, (), 1.0, []]
    for value in values:
        with pytest.raises(TypeError) as t:
            score([value])
        assert str(t.value) == 'Only integers accepted!'


def test_1():
    invoke = score([1])
    assert invoke == 'odds win'


def test_2():
    invoke = score([2])
    assert invoke == 'even wins'


def test_tie():
    invoke = score([1, 2])
    assert invoke == 'tie'


def test_multiple_numbers():
    invoke = score([1, 2, 3, 4, 5])
    assert invoke == 'odds win'
