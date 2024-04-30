from katas.traverse_students import traverse_students
import pytest

students = [
    ['Joe',  'David', 'Alex', 'Danika', 'Cat', 'Verity'],
    ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan'],
    ['John', 'Dulcy', 'Bean', 'Dylan']
]
direction = ['up', 'down', 'left']


def test_student_list_only():
    values = [{}, 1, 'a', None, False, True]
    for value in values:
        with pytest.raises(TypeError) as t:
            traverse_students(value, ['up'])
        assert str(t.value) == 'List of lists only!'


def test_student_list_of_lists_only():
    value = [['hi'], 'a']
    with pytest.raises(TypeError) as t:
        traverse_students(value, ['up'])
    assert str(t.value) == 'Students must contain lists!'


def test_directions_must_be_list():
    direction = ['up']
    with pytest.raises(TypeError) as t:
        traverse_students([['john']], [1])
    assert str(t.value) == 'up, down, left, right only!'


def test_up_down_left_right_only():
    direction = ['dow', 'lef', 'u', 'ri']
    for d in direction:
        with pytest.raises(TypeError) as t:
            invoke = traverse_students([['john']], [d])
        assert str(t.value) == 'up, down, left, right only!'


def test_returns_a_list():
    invoke = traverse_students(students, direction)
    assert isinstance(invoke, list)


def test_up_from_start():
    invoke = traverse_students(students, ['up'])
    assert invoke == []


def test_down_from_start():
    invoke = traverse_students(students, ['down'])
    assert invoke == ['Hev']


def test_two_down_from_start():
    invoke = traverse_students(students, ['down', 'down'])
    assert invoke == ['Hev', 'John']


def test_down_exceeds_number_of_tables():
    invoke = traverse_students(
        students, ['down', 'down', 'down', 'down', 'down'])
    assert invoke == ['Hev', 'John']


def test_down_up():
    invoke = traverse_students(
        students, ['down', 'up'])
    assert invoke == ['Hev', 'Joe']


def test_down_up_exceed_start_pos():
    invoke = traverse_students(
        students, ['down', 'up', 'up', 'up'])
    assert invoke == ['Hev', 'Joe']


def test_left_from_start():
    invoke = traverse_students(
        students, ['left'])
    assert invoke == ['Verity']


def test_left_left_from_start():
    invoke = traverse_students(
        students, ['left', 'left'])
    assert invoke == ['Verity', 'Cat']


def test_left_x7_from_start():
    invoke = traverse_students(
        students, ['left', 'left', 'left', 'left', 'left', 'left', 'left'])
    assert invoke == ['Verity', 'Cat', 'Danika',
                      'Alex', 'David', 'Joe', 'Verity']


def test_right_from_start():
    invoke = traverse_students(
        students, ['right'])
    assert invoke == ['David']


def test_right_x10_from_start():
    invoke = traverse_students(
        students, ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'])
    assert invoke == ['David', 'Alex', 'Danika', 'Cat',
                      'Verity', 'Joe', 'David', 'Alex', 'Danika', 'Cat']


def test_up_down_left_right():
    invoke = traverse_students(
        students, ['down', 'right', 'right', 'up', 'left'])
    assert invoke == ['Hev', 'Carrie', 'Heather', 'Alex', 'David']
