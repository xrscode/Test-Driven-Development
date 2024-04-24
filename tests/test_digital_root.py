from katas.digital_root import digital_root
import pytest


def test_only_integers_accepted():
    values = [True, False, None, {}, [], '15']
    for value in values:
        with pytest.raises(TypeError) as t:
            digital_root(value)
        assert str(t.value) == f"Value is of type: {
            type(value)} only integers accepted!"


def test_returns_digital_root_for_1():
    invoke = digital_root(1)
    assert invoke == 1


def test_returns_digital_root_for_12():
    invoke = digital_root(12)
    assert invoke == 3


def test_returns_digital_root_for_10():
    invoke = digital_root(10)
    assert invoke == 1


def test_returns_digital_root_for_942_recursion_depth_2():
    invoke = digital_root(942)
    assert invoke == 6


def test_returns_digital_root_for_493193_recursion_depth_3():
    invoke = digital_root(493193)
    assert invoke == 2
