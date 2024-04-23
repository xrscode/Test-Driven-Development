from katas.convert_units import convert
import pytest


def test_only_accepts_integer():
    with pytest.raises(TypeError) as t:
        invoke = convert('a')
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_only_accepts_integer_larger_than_1():
    with pytest.raises(TypeError) as t:
        invoke = convert(0)
    assert str(t.value) == 'Must be an integer larger than 1!'


def test_returns_a_list():
    invoke = convert(1)
    assert isinstance(invoke, list)


def test_returns_single_num_in_list():
    invoke = convert(1)
    assert invoke == [1]


def test_returns_single_num_for_multiple_of_10():
    invoke = convert(10)
    assert invoke == [10]


def test_returns_two_nums():
    invoke = convert(11)
    assert invoke == [10, 1]


def test_returns_two_nums_for_101():
    invoke = convert(101)
    assert invoke == [100, 1]


def test_returns_three_nums_for_115():
    invoke = convert(115)
    assert invoke == [100, 10, 5]
