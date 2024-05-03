from katas.justify_line import justify
import pytest


def test_string_only():
    values = [1.0, 1, True, False, {}, [], None, ()]
    for value in values:
        with pytest.raises(TypeError) as t:
            justify(value, 1)
        assert str(t.value) == 'String for first argument only.'


def test_integer_for_second_argument():
    values = ['hi', 1.0, True, False, {}, [], None, ()]
    for value in values:
        with pytest.raises(TypeError) as t:
            justify('dog', value)
        assert str(t.value) == 'Integer for second argument only.'


def test_integer_exceeds_line_length():
    invoke = justify('hi', 1)
    assert invoke == 'String exceeds maximum line length.'


def test_one_padding_from_start():
    invoke = justify('foo foo foo foo', 16)
    assert invoke == 'foo  foo foo foo'


def test_two_equal_spaces():
    invoke = justify('foo foo foo foo', 18)
    assert invoke == 'foo  foo  foo  foo'


def test_three():
    invoke = justify('foo  foo  foo  foo', 20)
    assert invoke == 'foo   foo   foo  foo'
