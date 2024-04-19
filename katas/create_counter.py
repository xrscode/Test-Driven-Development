def clean_string(s):
    str_list = list(s)[::-1]
    new = []
    hash = 0
    for i, x in enumerate(str_list):
        if x == '#':
            hash += 1
        elif x.isalpha():
            if hash > 0:
                hash -= 1
                continue
            else:
                new.append(x)

    return ''.join(new[::-1])


print(clean_string('ab##cd#c'))
