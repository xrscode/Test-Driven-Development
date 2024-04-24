def count(num):
    """
    ARGS:
    Integer.

    RETURNS:
    Integer representing the sum
    of bits equal to 1
    in the binary representation of an integer.
    """
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError('Argument must be integer!')

    binary_str = str(bin(num)[2:])

    return binary_str.count('1')
