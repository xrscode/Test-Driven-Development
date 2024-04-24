from katas.detect_pangram import pangram
import pytest


def test_only_accepts_string_as_argument():
    values = [True, False, None, [], 1, 1.0, {}]
    for value in values:
        with pytest.raises(TypeError) as t:
            pangram(value)
        assert str(t.value) == 'String only!'


def test_returns_false_for_non_complete_alphabet():
    invoke = pangram('abcdefghijklmnopqrstuvwxy')
    assert invoke == False


def test_returns_true_for_complete_alphabet():
    invoke = pangram('abcdefghijklmnopqrstuvwxyz')
    assert invoke == True


def test_ignores_non_alphabet_letters():
    invoke = pangram('^%£&^((*&^%$£$%^%$£$%^')
    assert invoke == False


def test_works_for_sentences():
    invoke = pangram("The quick brown fox jumps over the lazy dog.")
    assert invoke == True
