def camel_case(string, boolean):
    if not isinstance(string, str):
        raise ValueError('First argument must be a string!')
    if not isinstance(boolean, bool):
        raise ValueError('Second argument must be a boolean!')

    split = string.split(' ')

    if boolean == True:
        for index, word in enumerate(split):
            split[index] = word[0].upper() + word[1:].lower()
    else:
        for index, word in enumerate(split):
            if index == 0:
                split[index] = word[0:].lower()
            else:
                split[index] = word[0].upper() + word[1:].lower()

    return ''.join(split)
