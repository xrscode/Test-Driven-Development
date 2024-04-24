def pangram(string):
    """
    ARGS:
    String.

    RETURNS:
    Boolean:
        # True if all letters of alphabet present.
        # False if not all letters of alphabet present
    """
    if not isinstance(string, str):
        raise TypeError('String only!')

    list = []

    for char in string:
        if char.lower() not in list and char.isalpha():
            list.append(char)
            if len(list) == 26:
                return True
    return False
