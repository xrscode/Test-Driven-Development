import math


def convert(num):
    if not isinstance(num, int) or num <= 0:
        raise TypeError('Must be an integer larger than 1!')

    units = []

    while len(str(num)) > 1:
        divisor = int(1*10**(len(str(num)))/10)
        quantity = math.floor(num / divisor)
        units.append(int(quantity * divisor))
        num = num % divisor

    if num == 0:
        return units
    else:
        units.append(num)

    return units


print(convert(235))
