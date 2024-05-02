def encrypt(string, integer):
    """
    Args:
    String and an integer.

    Returns:
    Given string S and integer N:
    function concatenates all odd-indexed characters
    of S with all the even-index characters of S.
    Repeats N times.
    """
    if not isinstance(string, str):
        raise TypeError('String only for first argument!')
    elif not isinstance(integer, int) or isinstance(integer, bool):
        raise TypeError('Integer only for second argument!')
    elif not string.isnumeric():
        raise TypeError('String must contain integers!')

    if integer == 0:
        return string
    elif integer > 0:
        ls = list(string)
        pos = ''
        neg = ''
        for i, num in enumerate(ls):
            if i % 2:
                pos += num
            else:
                neg += num
        new = pos + neg
        integer -= 1
        return encrypt(new, integer)
