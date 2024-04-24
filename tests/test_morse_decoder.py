from katas.morse_decoder import decode
import pytest


def test_only_accepts_string_as_argument():
    values = [True, False, None, {}, 1, 1.0, []]
    for value in values:
        with pytest.raises(TypeError) as t:
            decode(value)
        assert str(t.value) == 'String only!'


def test_returns_string():
    invoke = decode('.-')
    assert isinstance(invoke, str)


def test_decodes_single_letter():
    invoke = decode('.-')
    assert invoke == 'A'


def test_checks_alphabet():
    morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
                      '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i, letter in enumerate(morse_alphabet):
        invoke = decode(letter)
        assert invoke == alphabet[i]


def test_ignores_non_alphabet():
    invoke = decode('!')
    assert invoke == '!'


def test_phrase():
    invoke = decode('--. --- --- -..    -- --- .-. -. .. -. --.')
    assert invoke == 'GOOD MORNING'


def test_phrase_with_punctuation():
    invoke = decode('--. --- --- -.. ,    -- --- .-. -. .. -. --. !')
    assert invoke == 'GOOD, MORNING!'
