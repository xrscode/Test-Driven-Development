from katas.sum_ascii import sum_ascii
import pytest

def test_error_if_not_list():
    with pytest.raises(TypeError) as t:
        invoke = sum_ascii('dog')
    assert str(t.value) == 'Must be a string!'

def test_error_if_list_length_0():
    with pytest.raises(ValueError) as t:
        invoke = sum_ascii([])
    assert str(t.value) == 'Must be a string!'

def test_error_non_string_present_in_list():
    with pytest.raises(ValueError) as t:
        invoke = sum_ascii([1, 'a'])
    assert str(t.value) == 'Must be a string!'

def test_returns_a_string():
    invoke = sum_ascii(['a'])
    assert isinstance(invoke, str)

def test_returns_ascii_val_for_one_char():
    invoke = sum_ascii(['a'])
    assert invoke == '97'

def test_returns_highest_ascii_char():
    invoke = sum_ascii(['a', 'b'])
    assert invoke == 'b = 98'

def test_returns_highest_ascii_char_no_duplicates():
    invoke = sum_ascii(['a', 'b', 'b'])
    assert invoke == 'b = 98'

def test_returns_more_names_if_ascii_same():
    invoke = sum_ascii(['abc', 'cba'])
    assert invoke == 'b = 98'