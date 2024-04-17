from katas.get_distinct_letters import distinct_letters
import pytest

"""
## Args:
Two strings.
distinct_letters('hello', 'daniel')
---
## Returns:
---
Returns a string of letters unique to either input string.
String will be in alphabetical order. 
Values sorted by ASCII code incase of non alpha/numeric characters.
"""


def test_only_accepts_string_first_argument():
    with pytest.raises(ValueError) as v:
        invoke = distinct_letters(1, 'a')
        print(str(v.value))
        assert str(v.value) == 'Values must be strings.'


def test_only_accepts_string_second_argument():
    with pytest.raises(ValueError) as v:
        invoke = distinct_letters('a', 2)
        print(str(v.value))
        assert str(v.value) == 'Values must be strings.'


def test_returns_one_char_present_in_both_strings():
    invoke = distinct_letters('a', 'a')
    assert invoke == 'a'


def test_upper_lower_case_chars_considered_same_converted_to_lower():
    invoke = distinct_letters('Aa', 'b')
    assert invoke == 'a'


def test_returns_unique_chars_ignores_case():
    invoke = distinct_letters('B', 'a')
    assert invoke == 'ab'


def test_arranges_numeric_numbers_first():
    invoke = distinct_letters('a1', 'b')
    assert invoke == '1ab'


def test_sorts_longer_sentences():
    one = 'hello'
    two = 'world'
    invoke = distinct_letters(one, two)
    assert invoke == 'dehrw'


def test_ignores_non_alphanumeric_numbers():
    one = 'HHELLLOOO*'
    two = '56world'
    invoke = distinct_letters(one, two)
    assert invoke == '56dehrw'
