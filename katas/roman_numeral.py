def encode(num):
    if not isinstance(num, int) or num <= 0:
        raise TypeError('Must be an integer larger than 1!')
    elif num > 1000:
        raise ValueError('Value must be less than 1000!')

    num_str = str(num)

    numeral_str = ''

    roman_dict = {1: 'I', 2: 'II', 3: 'III',
                  4: 'IV', 5: 'V', 6: 'VI',
                  7: 'VII', 8: 'VIII', 9: 'IX',
                  10: 'X', 20: 'XX', 30: 'XXX',
                  40: 'XL', 50: 'L', 60: 'LX',
                  70: 'LXX', 80: 'LXXX', 90: 'XC',
                  100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC',
                  700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'}

    # Convert to list of units:
    number_list = [int(x + '0' * (len(num_str[i:])-1))
                   for i, x in enumerate(num_str) if x != '0']

    for x in number_list:
        numeral_str += roman_dict[x]

    return numeral_str
