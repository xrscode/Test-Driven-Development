def score(lst):
    """
    Args:
    Accepts a list of even and odd positive numbers.

    Returns:
    If number is odd; converted to binary code.  Count 1's.
    If number is even; convert to binary code.  Count 0's.
    If more odd 1's then odd wins.  If more 0's then even wins.
    Returns:
    'odd wins', 'even wins' or 'tie' string based upon scores.
    """
    # Only accept list:
    if not isinstance(lst, list):
        raise TypeError('List only!')
    # List must contain integers only:
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in lst):
        raise TypeError('Only integers accepted!')

    odd = 0
    even = 0

    for num in lst:
        if num % 2:
            one_quant = 0
            binary = str(bin(num).lstrip('-0b'))
            count = binary.count('1')
            print(binary, count, '1')
            odd += count

        else:
            one_quant = 0
            binary = str((bin(num).lstrip('-0b')))
            count = binary.count('0')
            print(binary, count, '0')
            even += count

    if odd == even:
        return 'tie'
    elif odd > even:
        return 'odds win'
    else:
        return 'even wins'
