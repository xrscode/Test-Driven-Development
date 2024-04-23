def encode(num):
    if not isinstance(num, int) or num <= 0:
        raise TypeError('Must be an integer larger than 1!')

    numeral_str = ''

    start_divison = int(1 * 10**(len(str(num)))/10)

    print(num / 1)

    return numeral_str


print(encode(1))
print(encode(2))
print(encode(3))
print(encode(4))
print(encode(5))
print(encode(6))
