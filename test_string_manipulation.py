from string_manipulation import manipulate_string
import pytest


def test_remove_chars():
    name = 'Raphael'
    name = manipulate_string(name)
    assert name == 'aphae'


def test_short_string():
    value = 'ab'
    value = manipulate_string(value)
    assert value == 'ba'


def test_invalid_string():
    value = '1'

    with pytest.raises(ValueError):
        value = manipulate_string(value)

    value = ''
    with pytest.raises(ValueError):
        value = manipulate_string(value)
