def justify(string, num):
    """
    Args:
    String of text and integer.
    Integer represents max line length.

    Returns:
    Returns text justified according to max line length - integer.

    If string contains mroe chars than max line length; function returns
    'String exceeds maximum line length.'

    Space between words padded with additional space so that final word
    in a line touches the edge of the line.  When distirbuting additional
    spaces, larger gaps should coem at the start of the line. 
    """
    if not isinstance(string, str):
        raise TypeError('String for first argument only.')
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError('Integer for second argument only.')

    # String length greter than number:
    line_length = len(string)
    if line_length >= num:
        return 'String exceeds maximum line length.'

    spaces_to_add = num - len(string)
    string = list(string)

    while spaces_to_add > 0:
        space = 0
        for i, char in enumerate(string):
            if char == ' ':
                space += 1
            if char.isalpha() and space > 0 and spaces_to_add > 0:
                space = 0
                string.insert(i-1, ' ')
                spaces_to_add -= 1

    return ''.join(string)
