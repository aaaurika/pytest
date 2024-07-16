import pytest

from number_set import NumberSet  # импортируем класс из файла number_set.py

def test_sum():
    set = NumberSet([1, 2, 3, 4, 5])
    assert set.sum() == 15

def test_mean():
    set = NumberSet([1, 2, 3, 4, 5])
    assert set.mean() == 3

def test_maximum():
    set = NumberSet([1, 2, 3, 4, 5])
    assert set.maximum() == 5

def test_minimum():
    set = NumberSet([1, 2, 3, 4, 5])
    assert set.minimum() == 1

def test_empty_set():
    set = NumberSet([])
    assert set.sum() == 0
    assert set.mean() == 0  # среднее от пустого набора равно 0
    with pytest.raises(ValueError):
        set.maximum()
    with pytest.raises(ValueError):
        set.minimum()
