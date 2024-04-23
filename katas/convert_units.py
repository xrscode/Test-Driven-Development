def convert(num):
    if not isinstance(num, int) or num <= 0:
        raise TypeError('Must be an integer larger than 1!')

    start_division = int(1 * 10**(len(str(num)))/10)

    units = []

    while num > 0:
        a = int(num / start_division)
        zero = ['0' for x in range(0, len(str(a)))]
        units.append(f"{a} * 1{''.join(zero)}")
        num -= a * int(zero[0])
        try:
            start_division = int(start_division/10)
        except:
            return ''.join(units)

    return ''.join(units)


print(convert(90))
