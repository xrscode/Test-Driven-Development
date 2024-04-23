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


def test_negative_shift_by_one_place():
    invoke = caesar('A', -1)
    assert invoke == 'z'


def test_negative_shift_by_two_place():
    invoke = caesar('A', -2)
    assert invoke == 'y'


def test_negative_shift_A_by_58_places():
    invoke = caesar('A', -58)
    assert invoke == 'A'


def test_negative_A_shift_by_59_places():
    invoke = caesar('A', -59)
    assert invoke == 'z'


def test_shifts_a_letter_by_one_place():
    invoke = caesar('a', 1)
    assert invoke == 'b'


def test_shifts_z_letter_by_one_place():
    invoke = caesar('z', 1)
    assert invoke == 'A'


def test_shifts_one_letter_by_one_57_places():
    invoke = caesar('A', 57)
    assert invoke == 'z'


def test_shifts_one_letter_by_58_places():
    invoke = caesar('A', 58)
    assert invoke == 'A'


def test_ignores_non_alphabetical_chars():
    invoke = caesar('£ $%', 10)
    assert invoke == '£ $%'


def test_for_sentence_positive_displacement():
    invoke = caesar('Hello World!', 10)
    assert invoke == 'Rovvy ayBvn!'


def test_for_sentence_negative_displacement():
    invoke = caesar('Hello World!', 10)
    assert invoke == 'Rovvy ayBvn!'
