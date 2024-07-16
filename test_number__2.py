import pytest

from number_set_2 import Number  

def test_set_and_get_value():
    number = Number(10)
    assert number.get_value() == 10
    number.set_value(20)
    assert number.get_value() == 20

def test_to_octal():
    number = Number(10)
    assert number.to_octal() == '0o12'

def test_to_hexadecimal():
    number = Number(10)
    assert number.to_hexadecimal() == '0xa'

def test_to_binary():
    number = Number(10)
    assert number.to_binary() == '0b1010'
