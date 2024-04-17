from katas.get_years_of_growth import get_years_of_growth
import pytest

"""
The function get_years_of_growth should take 4 parameters: a starting population, an end population, a percentage of growth and a netMigration figure.

If the population grows by the given percentage each year, plus an additional number of net migrants, the function should calculate how many years it takes until the end population total is reached.

e.g: getYearsOfGrowth(1000, 2000, 2, 12) # 25
"""


def test_end_not_larger_than_start():
    with pytest.raises(ValueError) as v:
        invoke = get_years_of_growth(10, 5, 5, 5)
        assert str(v.value) == 'End year can not be less than start year!'


def test_start_must_be_integer():
    s = 'a'
    e = 5
    p = 5
    m = 5
    with pytest.raises(TypeError) as e:
        invoke = get_years_of_growth(s, e, p, m)
        assert str(e.value) == 'Only integers accepted!'


def test_end_is_integer():
    with pytest.raises(TypeError) as e:
        end = get_years_of_growth(5, 'a', 5, 5)
        assert str(e.value) == 'Only integers accepted!'


def test_percent_is_integer():
    with pytest.raises(TypeError) as e:
        percent = get_years_of_growth(5, 5, 'a', 5)
        assert str(e.value) == 'Only integers accepted!'


def test_migration_is_integer():
    with pytest.raises(TypeError) as e:
        migration = get_years_of_growth(5, 5, 5, 'a')
        assert str(e.value) == 'Only integers accepted!'


def test_start_100_end_101_percent_1():
    start = 100
    end = 101
    percent = 1
    migration = 0
    invoke = get_years_of_growth(start, end, percent, migration)
    assert invoke == 1


def test_start_100_end_110_percent_1_migration_5():
    start = 100
    end = 110
    percent = 1
    migration = 5
    invoke = get_years_of_growth(start, end, percent, migration)
    assert invoke == 2


def test_1000_2000_2_12():
    start = 1000
    end = 2000
    percent = 2
    migration = 12
    invoke = get_years_of_growth(start, end, percent, migration)
    assert invoke == 25
