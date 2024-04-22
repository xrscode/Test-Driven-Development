from katas.caesar_cipher import caesar
import pytest

def test_first_argument_must_be_string():
    with pytest.raises(TypeError) as t:
        invoke = caesar(1, 1)
    assert str(t.value) == 'First argument must be a string!'


def test_second_argument_must_be_integer():
    with pytest.raises(TypeError) as t:
        invoke = caesar('a', 'a')
    assert str(t.value) == 'Second argument must be an integer!'

def test_returns_a_string():
    invoke = caesar('a', 1)
    assert isinstance(invoke, str)

def test_shifts_one_letter_by_one_place():
    invoke = caesar('a', 1)
    assert invoke == 'b'