import re


def crack(string):
    # TRY to Extract code from paraenthesis:
    if not isinstance(string, str):
        raise TypeError('String only.')
    else:
        try:
            code = re.search(r'\((.*?)\)', string)
            if code is None:
                # No match as no paranthesis.
                raise ValueError('No paranthesis detected!')
            if len(code.group(1)) == 0:
                # Match as paranthesis exist, but no code present.
                raise ValueError('No code detected!')
            code = re.search(r'\((.*?)\)', string).group(1)
        except ValueError as ve:
            raise ve

    # Extract start of code:
    start = string[:-(len(code)) + 2]

    common_dict = {}

    for char in start:
        if not char.isalpha():
            continue
        else:
            if char not in common_dict:
                common_dict[char] = 1
            else:
                common_dict[char] += 1

    # Sort Dictionary by Value and create list of tuples.
    sorted_occurences = dict(sorted(
        common_dict.items(), key=lambda item: item[1], reverse=True))

    common_list = []

    # Establish most common letters.
    # aaa-bbb-ccc-d-e-f, common letters are: a, b, c, d, e, f.
    # aaa-bbb-ccc-dd-e-f, common letters are: a, b, c, d.
    # aaa-bbb-ccc-ddd-eee-fff, common letters are: a, b, c, d, e, f.
    for x in sorted_occurences:
        if len(common_list) < len(code):
            common_list.append(x)
        elif len(common_list) >= len(code):
            final_char = common_list[len(code) - 1]
            final_val = sorted_occurences[final_char]
            if final_val == sorted_occurences[x]:
                common_list.append(x)
            else:
                break

    # Create string out of sorted code
    sorted_code = ''.join(sorted(code))

    # If code is alphabetical and all letters are in common_list:
    if ''.join(sorted_code) == code and all(
            char in common_list for char in code):
        return True
    return False
