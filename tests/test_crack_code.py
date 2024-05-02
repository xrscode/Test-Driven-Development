from katas.crack_code import crack
import pytest


def test_string_only():
    values = [1, 1.0, True, False, None, {}, []]
    for value in values:
        with pytest.raises(TypeError) as t:
            crack(value)
        assert str(t.value) == 'String only.'


def test_code_present():
    with pytest.raises(ValueError) as v:
        crack('aaa-bbb-ccc-ddd()')
    assert str(v.value) == 'No code detected!'


def test_paranthesis_present():
    with pytest.raises(ValueError) as v:
        crack('aaa-bbb-ccc-ddd')
    assert str(v.value) == 'No paranthesis detected!'


def test_simple_code_alphabetical_order():
    test_string = 'a-b-c-d(abcd)'
    invoke = crack(test_string)
    assert invoke


def test_simple_code_non_alphabetical_order():
    test_string = 'a-b-c-d(bacd)'
    invoke = crack(test_string)
    assert invoke == False


def test_multiple_common_chars():
    test_string = 'abcdefghijklmnop(film)'
    invoke = crack(test_string)
    assert invoke


def test_multiple_common_chars_non_alphabetical_code():
    test_string = 'abcdefghijklmnop(mlif)'
    invoke = crack(test_string)
    assert invoke == False
