def sum_ascii(ls):
    if not isinstance(ls, list):
        raise TypeError('Must be list!')
    else:
        if not len(ls):
            raise ValueError('List must be populated!')
        else:
            if not all(isinstance(val, str) for val in ls):
                raise ValueError('List must contain strings!')

    highest = 0
    name_highest = []

    for name in ls:
        ascii_values = [ord(x.lower()) for x in name]
        total = sum(ascii_values)

        if total > highest:
            highest = total
            name_highest = [name]
        
        elif total == highest:
            name_highest.append(name)

    unique = set(name_highest)

    return f"{', '.join(unique)} = {highest}"