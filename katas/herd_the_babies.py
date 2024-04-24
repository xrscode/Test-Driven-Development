def herd_the_babies(st):
    if not isinstance(st, str):
        raise TypeError('Must be a string!')

    dict = {
        'A': 0,
        'a': 0,
        'B': 0,
        'b': 0,
        'C': 0,
        'c': 0,
        'D': 0,
        'd': 0,
        'E': 0,
        'e': 0,
        'F': 0,
        'f': 0,
        'G': 0,
        'g': 0,
        'H': 0,
        'h': 0,
        'I': 0,
        'i': 0,
        'J': 0,
        'j': 0,
        'K': 0,
        'k': 0,
        'L': 0,
        'l': 0,
        'M': 0,
        'm': 0,
        'N': 0,
        'n': 0,
        'O': 0,
        'o': 0,
        'P': 0,
        'p': 0,
        'Q': 0,
        'q': 0,
        'R': 0,
        'r': 0,
        'S': 0,
        's': 0,
        'T': 0,
        't': 0,
        'U': 0,
        'u': 0,
        'V': 0,
        'v': 0,
        'W': 0,
        'w': 0,
        'X': 0,
        'x': 0,
        'Y': 0,
        'y': 0,
        'Z': 0,
        'z': 0
    }
    dict_non_alpha = {}

    for i, char in enumerate(st):
        if char.isalpha():
            dict[char] += 1
        else:
            dict_non_alpha[i] = char

    str_sort = ''

    for char in dict:
        while dict[char] > 0:
            dict[char] -= 1
            str_sort += char

    to_list = list(str_sort)

    for char in dict_non_alpha:
        to_list.insert(char, dict_non_alpha[char])

    return ''.join(to_list)
