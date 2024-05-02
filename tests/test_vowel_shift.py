from katas.vowel_shift import shift
import pytest


def test_returns_a_string():
    assert isinstance(shift('hello', 1), str)


def test_string_first_argument():
    values = [True, False, None, [], {}, 1, 1.0]
    for value in values:
        with pytest.raises(TypeError) as t:
            shift(value, 1)
        assert str(
            t.value) == 'Argument 1 must be a string!'
    assert isinstance(shift('hello', 1), str)


def test_int_first_argument():
    values = [True, False, None, [], {}, 1.5, 1.0]
    for value in values:
        with pytest.raises(TypeError) as t:
            shift('hello', value)
        assert str(
            t.value) == 'Argument 2 must be an integer!'
    assert isinstance(shift('hello', 1), str)


def test_return_string_if_integer_0():
    assert shift('hello', 0) == 'hello'


def test_shift_by_1():
    assert shift('hello', 1) == 'holle'


def test_shift_by_2():
    assert shift('star nosed mole', 2) == 'stor nesad mole'


def test_shift_by_4():
    assert shift('funnily enough', 4) == 'finnely onuugh'


def test_not_case_sensitive():
    assert shift('fUnnIly EnOUgh', 4) == 'fInnEly OnUUgh'


def test_negative_shift():
    assert shift('hello', -1) == 'holle'


def test_negative_shift_2():
    assert shift('star nosed mole', -2) == 'ster nosed malo'
