from katas.get_frequencies import get_frequencies
import pytest

"""
## Args:
One string
get_frequencies('hello my name is Dylan')
---
## Returns:
---
Dictionary with frequency of individual chars.
"""


def test_rejects_non_strings():
    with pytest.raises(ValueError) as v:
        invoke = get_frequencies(12345)
    assert str(v.value) == 'Argument must be a string!'


def test_returns_dictionary():
    invoke = get_frequencies('a')
    assert isinstance(invoke, dict) == True


def test_returns_dictionary_with_frequency_count():
    invoke = get_frequencies('a')
    assert invoke == {'a': 1}


def test_returns_dictionary_with_frequency_count_respects_case():
    invoke = get_frequencies('aA')
    assert invoke == {'a': 1, 'A': 1}


def test_returns_dictionary_with_frequency_count_respects_case_ignores_spaces():
    invoke = get_frequencies('a A')
    assert invoke == {'a': 1, 'A': 1}


def test_returns_frequency_count_for_sentence():
    invoke = get_frequencies('hello world')
    assert invoke == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
