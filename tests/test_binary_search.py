from katas.binary_search import binary_search_recursion
import pytest
import random

# Non Recursive Testing:
# def test_returns_TypeError_if_value_exceeds_list_final_value():
#     list = [i for i in range(1, 11)]
#     with pytest.raises(TypeError) as excinfo:
#         invoke = binary_search(list, 12)
#         assert str(excinfo.value) == 'Value too large.'


# def test_returns_TypeError_if_value_smaller_list_first_value():
#     list = [i for i in range(1, 11)]
#     with pytest.raises(TypeError) as excinfo:
#         invoke = binary_search(list, 0)
#         assert str(excinfo.value) == 'Value too small.'


# def test_n_is_an_integer():
#     # List = [1, 2, 3...10]
#     list = [i for i in range(1, 11)]
#     with pytest.raises(TypeError) as excinfo:
#         invoke = binary_search(list, 'a')
#         assert str(excinfo.value) == 'Value must be an integer.'


# def test_for_small_odd_length_list_where_n_is_mid_number():
#     # List = [1, 2, 3]
#     list = [i for i in range(1, 4)]
#     invoke = binary_search(list, 2)
#     assert invoke == 1


# def test_for_small_odd_length_list_where_n_is_final_number():
#     # List = [1, 2, 3]
#     list = [i for i in range(1, 4)]
#     invoke = binary_search(list, 3)
#     assert invoke == 2


# def test_for_small_odd_length_list_where_n_is_first_number():
#     # List = [1, 2, 3]
#     list = [i for i in range(1, 4)]
#     invoke = binary_search(list, 1)
#     assert invoke == 0


# def test_for_list_between_1_to_100_with_random_num():
#     # List = [1, 2, 3...100]
#     list = [i for i in range(1, 100)]
#     # Rand int between 1 - 100
#     number = round(random.random()*99) + 1
#     invoke = binary_search(list, number)
#     assert invoke == number - 1


# def test_for_list_between_1_to_10000_with_random_num():
#     # List = [1, 2, 3...100]
#     list = [i for i in range(1, 10000)]
#     # Rand int between 1 - 100
#     number = round(random.random()*99) + 1
#     invoke = binary_search(list, number)
#     assert invoke == number - 1


# Recursive Testing:
def test_recursive_for_small_odd_length_list_where_n_is_mid_number():
    # List = [1, 2, 3]
    list = [i for i in range(1, 4)]
    number = 2
    invoke = binary_search_recursion(list, number)
    assert invoke == 1


def test_recursive_for_small_odd_length_list_where_n_is_final_number():
    # List = [1, 2, 3]
    list = [i for i in range(1, 4)]
    number = 3
    invoke = binary_search_recursion(list, number)
    assert invoke == 2


def test_recursive_for_small_odd_length_list_where_n_is_first_number():
    # List = [1, 2, 3]
    list = [i for i in range(1, 4)]
    invoke = binary_search_recursion(list, 1)
    assert invoke == 0


def test_recursive_for_list_between_1_to_100_with_random_num():
    # List = [1, 2, 3...100]
    list = [i for i in range(1, 100)]
    # Rand int between 1 - 100
    number = round(random.random()*99) + 1
    invoke = binary_search_recursion(list, number)
    assert invoke == number - 1


def test_recursive_for_list_between_1_to_10000_with_random_num():
    # List = [1, 2, 3...100]
    list = [i for i in range(1, 10000)]
    # Rand int between 1 - 100
    number = round(random.random()*99) + 1
    invoke = binary_search_recursion(list, number)
    assert invoke == number - 1
