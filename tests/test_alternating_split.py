from katas.alternating_split import encrypt
import pytest


def test_type_value_error_for_first_arg():
    values = [1, 1.0, True, False, {}, [], 0, ()]
    for value in values:
        with pytest.raises(TypeError) as t:
            encrypt(value, 1)
        assert str(t.value) == 'String only for first argument!'


def test_type_value_error_for_second_arg():
    values = [True, False, {}, [], ()]
    for value in values:
        with pytest.raises(TypeError) as t:
            encrypt('012345', value)
        assert str(t.value) == 'Integer only for second argument!'


def test_type_value_error_for_first_arguemnt_non_integer_values_as_string():
    values = ['True', 'False', '{}', '[]', "()", "X@", '12a']
    for value in values:
        with pytest.raises(TypeError) as t:
            encrypt(value, 1)
        assert str(t.value) == 'String must contain integers!'


def test_returns_string():
    invoke = encrypt('012345', 1)
    assert isinstance(invoke, str)


def test_returns_string_all_numeric():
    invoke = encrypt('012345', 1)
    assert invoke.isnumeric()


def test_shift_1():
    invoke = encrypt('012345', 1)
    assert invoke == '135024'


def test_shift_2():
    invoke = encrypt('012345', 2)
    assert invoke == '304152'


def test_shift_3():
    invoke = encrypt('012345', 3)
    assert invoke == '012345'
