def traverse_students(student, directions):
    """
    Args:
    A list of students (strings):
    # [['Joe', 'David], ['Dylan', 'Billie']]
    A list of directions (strings):
    # ['right', 'right', 'up', 'left', 'down']

    Returns:
    A list of all students passed over. 
    """
    if not isinstance(student, list):
        raise TypeError('List of lists only!')
    elif not all(isinstance(x, list) for x in student):
        raise TypeError('Students must contain lists!')

    if not isinstance(directions, list):
        raise TypeError('Directions must be in a list!')
    elif not all(isinstance(x, str) for x in directions) or not all(x.lower() == 'up' or x.lower() == 'down' or x.lower() == 'left' or x.lower() == 'right' for x in directions):
        raise TypeError('up, down, left, right only!')

    current_index = [0, 0]

    student_list = []

    for direction in directions:
        if direction == 'up' and current_index[0] > 0:
            current_index[0] -= 1
            student_list.append(student[current_index[0]][current_index[1]])
        elif direction == 'up' and current_index[0] == 0:
            # Continue as no change
            continue
        elif direction == 'down' and current_index[0] < len(student) - 1:
            print('HERE', current_index)
            current_index[0] += 1
            student_list.append(student[current_index[0]][current_index[1]])
        elif direction == 'down' and current_index[0] == len(student) - 1:
            # Continue as no change
            continue
        elif direction == 'left':
            if current_index[1] == 0:
                new_index = len(student[current_index[0]]) - 1
                student_list.append(student[current_index[0]][new_index])
                current_index[1] = new_index
            else:
                current_index[1] -= 1
                student_list.append(
                    student[current_index[0]][current_index[1]])
        elif direction == 'right':
            if current_index[1] == len(student[current_index[0]]) - 1:
                current_index[1] = 0
                student_list.append(
                    student[current_index[0]][current_index[1]])
            else:
                current_index[1] += 1
                student_list.append(
                    student[current_index[0]][current_index[1]])

    return student_list


# print(traverse_students([['john']], ['DOwn']))
