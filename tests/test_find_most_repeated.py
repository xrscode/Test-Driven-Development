from katas.find_most_repeated import repeated
import pytest


def test_list_only_accepted():
    values = [1, 'a', {}, None, False, True]
    for value in values:
        with pytest.raises(TypeError) as t:
            invoke = repeated(value)
        assert str(t.value) == 'List only!'


def test_only_strings_and_ints():
    vals = [{}, None, True, False]
    for value in vals:
        with pytest.raises(ValueError) as v:
            repeated([value, 'str', 1])
        assert str(v.value) == 'Only string or integers!'


def test_returns_dictionary():
    invoke = repeated(['a'])
    assert invoke == {'elements': ['a'], 'repeats': 1}


def test_returns_max_number_of_elements():
    invoke = repeated(['a', 'a', 'a', 'b', 'c'])
    assert invoke == {'elements': ['a'], 'repeats': 3}


def test_returns_max_number_of_elements_if_repeated_max_element():
    invoke = repeated(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd'])
    assert invoke == {'elements': ['a', 'b', 'c'], 'repeats': 3}
