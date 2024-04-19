from katas.lengthen_date import lengthen_date
import pytest

"""
## Args:
Date string in the format: '21.03.2017'
---
## Returns:
---
String: 'Tuesday 21st March 2017'

## Dependencies:
---
from datetime import datetime
"""


def test_must_return_string():
    invoke = lengthen_date('21.03.2017')
    assert isinstance(invoke, str) == True


def test_rejects_non_string_arguments():
    with pytest.raises(TypeError) as t:
        lengthen_date(1)
    assert str(t.value) == 'String required!'


def test_rejects_non_valid_dates():
    # Test day:
    with pytest.raises(ValueError) as v:
        lengthen_date('33.03.2017')
    assert str(v.value) == 'Must be a valid date!'
    # Test month:
    with pytest.raises(ValueError) as v:
        lengthen_date('10..2017')
    assert str(v.value) == 'Must be a valid date!'
    # Test year:
    with pytest.raises(ValueError) as v:
        lengthen_date('10.1.')
    assert str(v.value) == 'Must be a valid date!'


def test_performs_mild_format_correction():
    # If '/' is used instead of '.':
    invoke = lengthen_date('21/04/1957')
    assert invoke == 'Sunday 21st April 1957'


def test_checks_day_battle_of_hastings():
    invoke = lengthen_date('14.10.1066')
    assert invoke == 'Sunday 14th October 1066'
