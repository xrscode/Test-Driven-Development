def alphabet_position(abc):
    """
    ARGS:
    String

    RETURNS:
    String representing position of each letter
    in alphabet.  Non alphabet character ignored.
    """
    if not isinstance(abc, str):
        raise TypeError('Argument must be string!')

    pos_list = [str(ord(x.lower()) - 96) if x.isalpha()
                else x for x in abc if x != ' ']

    return ' '.join(pos_list)
