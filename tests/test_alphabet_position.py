from katas.alphabet_position import alphabet_position
import pytest


def test_only_accepts_string():
    values = [1, False, True, None, [], {}, ()]
    for val in values:
        with pytest.raises(TypeError) as t:
            alphabet_position(val)
        assert str(t.value) == 'Argument must be string!'


def test_returns_a_string():
    invoke = alphabet_position('a')
    assert isinstance(invoke, str)


def test_returns_position_of_a():
    invoke = alphabet_position('a')
    assert invoke == '1'


def test_returns_position_of_z():
    invoke = alphabet_position('z')
    assert invoke == '26'


def test_returns_non_alphabet_char():
    values = ['!', '@', '£', '$', '%', '^', '&', '*', '`']
    for value in values:
        invoke = alphabet_position(value)
        assert invoke == value


def test_ignores_case():
    values = ['A', 'B', 'C', 'Z']
    result = [1, 2, 3, 26]
    for i, value in enumerate(values):
        invoke = alphabet_position(value)
        assert invoke == str(result[i])


def test_sentence():
    invoke = alphabet_position("The sunset sets at twelve o' clock.")
    assert invoke == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 ' 3 12 15 3 11 ."
