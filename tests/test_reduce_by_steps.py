from katas.reduce_by_steps import reduce
import pytest

# Functions:


def multiply(num1, num2):
    return num1 * num2


def sentence(str1, str2):
    return f"{str1} {str2}"


def test_first_argument_must_be_function():
    values = [0, True, False, {}, [], 'Hi', 1.0, None]
    for value in values:
        with pytest.raises(TypeError) as t:
            reduce(value, [], 0)
        assert str(t.value) == 'Function required for first argument!'


def test_second_argument_must_be_list():
    values = [0, True, False, {}, 'Hi', 1.0, None]
    for value in values:
        with pytest.raises(TypeError) as t:
            def myfunc():
                return 1
            reduce(myfunc, value, 1)
        assert str(t.value) == 'List required for second argument!'


def test_final_argument_must_be_int_or_str():
    values = [True, False, {}, 1.0, None]
    for value in values:
        with pytest.raises(TypeError) as t:
            def myfunc():
                return 1
            reduce(myfunc, [], value)
        assert str(t.value) == 'Int or string for final argument!'
