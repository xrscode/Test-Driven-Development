def fill_square(ls):
    """
    ARGS:
    List of lists.

    RETURNS:
    Square matrix of lists.
    Matrix set by length of longest list.
    'None' filled for empty values.
    New lists created if required.
    """
    if not isinstance(ls, list) or not all(isinstance(x, list) for x in ls):
        raise ValueError('List of lists only!')

    longest_list = len(sorted(ls, key=len, reverse=True)[0])

    # Add empty lists if needed:
    if longest_list > len(ls):
        count = longest_list
        while count != len(ls):
            fill = [None] * longest_list
            ls.append(fill)

    # Check sub lists populated:
    for item in ls:
        if len(ls) == 1 and len(item) == 0:
            return [[None]]
        while len(item) != longest_list:
            item.append(None)

    return ls
