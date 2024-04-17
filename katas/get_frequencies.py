def get_frequencies(string):
    if not isinstance(string, str):
        raise ValueError('Argument must be a string!')
    dict = {}
    for char in string:
        if char == ' ':
            continue
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict
