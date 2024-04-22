from katas.bubble_sort import bubble_sort
import pytest

def test_only_accepts_lists():
    with pytest.raises(TypeError) as t:
        bubble_sort(1)
    assert str(t.value) == 'List required!'

def test_rejects_empty_list():
    with pytest.raises(ValueError) as v:
        bubble_sort([])
    assert str(v.value) == 'List must be populated!'

def test_rejects_non_integer_values():
    with pytest.raises(ValueError) as v:
        bubble_sort([1.0])
    assert str(v.value) == 'Values must be type integer!'

def test_returns_list():
    invoke = bubble_sort([1])
    assert isinstance(invoke, list)

def test_does_not_change_ordered_list():
    invoke = bubble_sort([1, 2, 3])
    assert invoke == [1, 2, 3]

def test_reverses_final_values_out_of_order():
    invoke = bubble_sort([1, 3, 2])
    assert invoke == [1, 2, 3]

def test_reverses_first_values_if_out_of_order():
    invoke = bubble_sort([2, 1, 3])
    assert invoke == [1, 2, 3]

def test_orders_small_list():
    invoke = bubble_sort([5, 4, 3, 2, 1])
    assert invoke == [1, 2, 3, 4, 5]

def orders_large_list():
    num_list = [83, 26, 497, 359, 761, 44, 686, 912, 208, 143,
674, 225, 839, 577, 123, 890, 314, 672, 555, 419,
198, 608, 497, 742, 669, 952, 788, 235, 58, 316,
521, 478, 927, 768, 353, 200, 891, 599, 145, 612,
354, 904, 122, 852, 893, 288, 633, 77, 878, 497,
321, 390, 42, 899, 458, 630, 544, 978, 190, 613,
257, 640, 238, 697, 860, 512, 725, 365, 930, 12,
175, 545, 911, 204, 303, 869, 881, 722, 761, 624,
987, 464, 359, 193, 496, 821, 94, 573, 127, 848,
139, 384, 523, 497, 925, 6, 750, 463, 836, 579]
    invoke = bubble_sort(num_list)
    assert invoke == [6, 12, 26, 42, 44, 58, 77, 83, 94, 122, 123, 127, 139, 143, 145, 175, 190, 193, 198, 200, 204, 208, 225, 235, 238, 257, 288, 303, 314, 316, 321, 353, 354, 359, 359, 365, 384, 390, 419, 458, 463, 464, 478, 496, 497, 497, 497, 497, 512, 521, 523, 544, 545, 555, 573, 577, 579, 599, 608, 612, 613, 624, 630, 633, 640, 669, 672, 674, 686, 697, 722, 725, 742, 750, 761, 761, 768, 788, 821, 836, 839, 848, 852, 860, 869, 878, 881, 890, 891, 893, 899, 904, 911, 912, 925, 927, 930, 952, 978, 987]
    