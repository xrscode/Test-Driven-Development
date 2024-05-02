def shift(string, integer):
    """
    Args:
    String and integer.

    Returns:
    String where all vowels shifted by integer amount.

    Hello, 1 >  Holle
    """

    if not isinstance(string, str):
        raise TypeError('Argument 1 must be a string!')
    elif not isinstance(integer, int) or isinstance(integer, bool):
        raise TypeError('Argument 2 must be an integer!')
    elif integer == 0:
        return string

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Create list of vowels from string:
    vowel_list = [x for x in string if x in vowels]

    # Establish amount to shift by:
    shift = integer
    if integer >= len(vowel_list):
        shift = integer % len(vowel_list)
    elif integer == len(vowel_list):
        shift = integer

    # Shift the list of vowels by shift amount:
    new = vowel_list[-shift:] + vowel_list[:-shift]

    string = list(string)

    return_str = ''
    for x in string:
        if x in vowels:
            return_str += new[0]
            new.pop(0)
        else:
            return_str += x

    return ''.join(return_str)
