from katas.count_bits import count
import pytest


def test_accepts_integer_only():
    values = [True, None, False, 'Hi', [], {}, 5.0]
    for value in values:
        with pytest.raises(TypeError) as t:
            invoke = count(value)
        assert str(t.value) == 'Argument must be integer!'


def test_works_for_integers_returns_integer():
    values = [1, 12, 123, 1234, 12345, 123456,
              1234567, 12345678, 123456789, 12345678910]
    results = [1, 2, 6, 5, 6, 6, 11, 12, 16, 21]
    for i, value in enumerate(values):
        invoke = count(value)
        assert invoke == results[i]
        assert isinstance(invoke, int)
