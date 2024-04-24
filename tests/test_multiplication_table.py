from katas.multiplication import multiplication_table
import pytest


def test_only_int():
    values = [True, None, {}, [], 'Hi', 1.4]
    for value in values:
        with pytest.raises(TypeError) as t:
            invoke = multiplication_table(value)
        assert str(t.value) == 'Integer only!'


def test_returns_list():
    invoke = multiplication_table(0)
    assert invoke == [[]]


def test_returns_list_of_lists():
    invoke = multiplication_table(3)
    assert all(isinstance(x, list) for x in invoke)


def test_value_0_is_i_for_all_values():
    invoke = multiplication_table(3)
    for i, value in enumerate(invoke):
        assert value[0] == i


def test_value_1_is_i_for_all_values_except_value_0():
    invoke = multiplication_table(3)
    for i, value in enumerate(invoke):
        if i == 0:
            assert value[1] == 1
        else:
            assert value[1] == i


def test_returns_populated_lists():
    invoke = multiplication_table(1)
    assert invoke == [[0, 1], [1, 1]]


def test_for_longer_values():
    invoke = multiplication_table(5)
    result = [[0, 1, 2, 3, 4, 5],
              [1, 1, 2, 3, 4, 5],
              [2, 2, 4, 6, 8, 10],
              [3, 3, 6, 9, 12, 15],
              [4, 4, 8, 12, 16, 20],
              [5, 5, 10, 15, 20, 25]]
    assert invoke == result
