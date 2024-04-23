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

        if b == 0:
            return a
        elif b < 0:
            multiple = math.ceil((letter - 122)/57)
            c = letter + (58 * multiple)
            new_str += chr(c)

        elif b > 0:
            multiple = math.ceil((letter - 122)/57)
            c = letter - (58 * multiple)
            new_str += chr(c)
    return new_str


print(caesar('z', -1), 'y')
print(caesar('A', -1), 'z')
