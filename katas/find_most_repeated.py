def repeated(lst):
    """
    Args:
    Flat list composed of strings or numbers

    Returns:
    A dictionary showing most repeated
    {elements: ['foo'], repeats: 2}
    """
    if not isinstance(lst, list):
        raise TypeError('List only!')
    else:
        if not all((isinstance(x, int) or isinstance(x, str)) and not isinstance(x, bool) for x in lst):
            raise ValueError('Only string or integers!')

    dict = {}

    for x in lst:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    max_value = max(dict.values())
    max_values = [x for x in dict if dict[x] == max_value]

    return {'elements': max_values, 'repeats': max_value}
