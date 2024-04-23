from katas.convert_units import convert
import pytest


def test_only_accepts_integer():
    with pytest.raises(TypeError) as t:
        invoke = convert('a')
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_only_accepts_integer_larger_than_1():
    with pytest.raises(TypeError) as t:
        invoke = convert(0)
    assert str(t.value) == 'Must be an integer larger than 1!'
