def multiplication_table(num):
    """
    ARGS:
    - Number
    RETURNS:
    Nested array representation of the
    multiplication table, including
    headlings of the table's rows and columns.
    """
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError('Integer only!')
    elif num < 0:
        num *= -1
    elif num == 0:
        return [[]]

    ls = []

    # Generate Empty Lists
    for x in range(num + 1):
        ls.append([])

    # Fill Empty Lists
    for i, x in enumerate(ls):
        if i == 0:
            for y in range(len(ls)):
                x.append(y)
        elif i > 0:
            x.append(i)
            x.append(i)
        while len(x) < len(ls):
            last = x[-1:][0]
            x.append(last + x[0])
    return ls
