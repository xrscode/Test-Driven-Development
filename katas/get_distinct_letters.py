def distinct_letters(str_one, str_two):
    if not all(isinstance(string, str) for string in (str_one, str_two)):
        raise ValueError('Values must be strings.')

    uniques = []

    for char in str_one:
        if char.lower() not in uniques and char.lower() not in str_two and char.isalnum():
            uniques.append(char.lower())

    for char in str_two:
        if char.lower() not in uniques and char.lower() not in str_one and char.isalnum():
            uniques.append(char.lower())

    # Sort by ASCII value
    uniques.sort(reverse=False)
    return ''.join(uniques)


print(distinct_letters('Aa4*', 'b'))
