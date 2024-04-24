def reduce(f, l, i):
    """
    Args:
    - Callable function.
    - List.
    - Initial value.

    Returns:
    - List reduced to single string or number. 
    - ['Let', 'us', 'work'] = 'Let us work'
    - [5, 4, 3, 2, 1] = 15
    """
    if not callable(f):
        raise TypeError('Function required for first argument!')
    pass

    if not isinstance(l, list):
        raise TypeError('List required for second argument!')

    if not (isinstance(i, str) or isinstance(i, int)) or isinstance(i, bool):
        raise TypeError('Int or string for final argument!')

    accumulator = i

    for x in l:
        accumulator = f(accumulator, x)

    return accumulator
