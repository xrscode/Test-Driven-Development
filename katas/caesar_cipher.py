import math


def caesar(a, b):
    if not isinstance(a, str):
        raise TypeError('First argument must be a string!')
    elif not isinstance(b, int):
        raise TypeError('Second argument must be an integer!')

    new_str = ''

    for letter in a:
        if not letter.isalpha():
            new_str += letter
            continue

        letter = ord(letter)
        letter += b

        if b < 0:
            multiple = math.floor((122-letter)/58)
            c = letter + (multiple * 58)
            new_str += chr(c)
        elif b > 0:
            multiple = math.ceil((letter - 122)/57)
            c = letter - (58 * multiple)
            new_str += chr(c)
        else:
            return a
    return new_str
