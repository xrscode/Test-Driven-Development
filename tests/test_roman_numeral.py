from katas.roman_numeral import encode
import pytest


def test_only_accepts_integer():
    with pytest.raises(TypeError) as t:
        invoke = encode('a')
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_only_accepts_integer_larger_than_1():
    with pytest.raises(TypeError) as t:
        invoke = encode(0)
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_returns_string():
    invoke = encode(1)
    assert isinstance(invoke, str)


def test_converts_1_to_I():
    invoke = encode(1)
    assert invoke == 'I'
