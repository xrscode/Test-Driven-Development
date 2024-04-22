import math
def caesar(a, b):
    if not isinstance(a, str):
        raise TypeError('First argument must be a string!')
    elif not isinstance(b, int):
        raise TypeError('Second argument must be an integer!')
    
    cipher = ''

    for char in a:
        if char.isalpha():
            print(ord(char), 'V')
            new_val = ord(char) + b
            print(new_val, 'x')
            if new_val > 122:
                multiple = math.floor(new_val / 57)
                new_val = new_val - (multiple * 57) + 57
                cipher += chr(new_val)
            elif new_val < 65:
                multiple = math.floor(new_val / 57 * -1)
                new_val = new_val + (56 * multiple)
                cipher += chr(new_val)
            else:
                cipher += chr(new_val)
        else:
            cipher += char
    return cipher



print(caesar('A', -1))
print(caesar('A', 1))