from katas.herd_the_babies import herd_the_babies
import pytest

def test_accepts_string():
    with pytest.raises(TypeError) as t:
        invoke = herd_the_babies(1)
    assert str(t.value) == 'Must be a string!'

def test_two_letters_lower_case():
    invoke = herd_the_babies('ba')
    assert invoke == 'ab'

def test_two_letters_upper_case():
    invoke = herd_the_babies('BA')
    assert invoke == 'AB'

def test_retain_position_of_non_alpha_characters():
    invoke = ['aA*', 'a*A', '*aA']
    result = ['Aa*', 'A*a', '*Aa']
    for i, x in enumerate(invoke):
        assert herd_the_babies(x) == result[i]

def test_simple_two_letters_one_uppercase_one_lowercase():
    invoke = herd_the_babies('aA')
    assert invoke == 'Aa'

def test_two_different_chars_upper_lower():
    invoke = herd_the_babies('Ba')
    assert invoke == 'aB'

def test_multiple_chars():
    invoke = ['xz*ZBar', 'a*czSDFGHvjoei2345Tx&$', '%%&6ifgdskng;ljh34p6q3aGSDGJ']
    result = ['aB*rxZz', 'a*cDeFGHijoSTv2345xz&$', '%%&6aDdfGGgg;hiJ34j6k3lnpqSs']
    for i, x in enumerate(invoke):
        assert herd_the_babies(x) == result[i]