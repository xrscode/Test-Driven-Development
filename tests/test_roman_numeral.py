from katas.roman_numeral import encode
import pytest


def test_only_accepts_integer():
    with pytest.raises(TypeError) as t:
        invoke = encode('a')
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_only_accepts_integer_larger_than_1():
    with pytest.raises(TypeError) as t:
        invoke = encode(0)
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_only_accepts_integer_1000_or_smaller():
    # Test 1000
    invoke_one = encode(1000)
    assert invoke_one == 'M'
    # Test 1001
    with pytest.raises(ValueError) as v:
        invoke = encode(1001)
    assert str(v.value) == 'Value must be less than 1000!'


def test_returns_string():
    invoke = encode(1)
    assert isinstance(invoke, str)


def test_converts_1_to_I():
    invoke = encode(1)
    assert invoke == 'I'


def test_converts_2_to_II():
    invoke = encode(2)
    assert invoke == 'II'


def test_converts_3_to_III():
    invoke = encode(3)
    assert invoke == 'III'


def test_converts_4_to_IV():
    invoke = encode(4)
    assert invoke == 'IV'


def test_converts_5_to_V():
    invoke = encode(5)
    assert invoke == 'V'


def test_converts_6_to_VI():
    invoke = encode(6)
    assert invoke == 'VI'


def test_converts_7_to_VII():
    invoke = encode(7)
    assert invoke == 'VII'


def test_converts_8_to_VIII():
    invoke = encode(8)
    assert invoke == 'VIII'


def test_converts_9_to_IX():
    invoke = encode(9)
    assert invoke == 'IX'


def test_converts_10_to_X():
    invoke = encode(10)
    assert invoke == 'X'
