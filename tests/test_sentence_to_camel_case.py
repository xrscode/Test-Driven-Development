from katas.sentence_to_camel_case import camel_case
import pytest
"""
## Args:
String and Boolean
---
## Returns:
---
Sentence to UpperCamelCase if True.
Sentence to lowerCamelCase if False.
"""


def test_first_argument_is_string():
    with pytest.raises(ValueError) as v:
        invoke = camel_case(1, True)
        assert str(v.value()) == 'First argument must be a string!'


def test_second_argument_is_boolean():
    with pytest.raises(ValueError) as v:
        invoke = camel_case('hello', 'False')
        assert str(v.value()) == 'Second argument must be a boolean!'


def test_single_lower_and_uppercase_to_uppercase():
    lower = 'a'
    upper = 'A'
    bool = True
    assert camel_case(lower, bool) == 'A'
    assert camel_case(upper, bool) == 'A'


def test_single_lower_and_uppercase_to_lowercase():
    lower = 'a'
    upper = 'A'
    bool = False
    assert camel_case(lower, bool) == 'a'
    assert camel_case(upper, bool) == 'a'


def test_sentence_to_upper_camel_case():
    str_one = 'hello my name is Dylan'
    str_two = 'HELLO MY NAME IS DYLAN'
    bool = False
    assert camel_case(str_one, bool) == 'helloMyNameIsDylan'
    assert camel_case(str_two, bool) == 'helloMyNameIsDylan'


def test_sentence_to_lower_camel_case():
    str_one = 'hello my name is Dylan'
    str_two = 'HELLO MY NAME IS DYLAN'
    bool = True
    assert camel_case(str_one, bool) == 'HelloMyNameIsDylan'
    assert camel_case(str_two, bool) == 'HelloMyNameIsDylan'
