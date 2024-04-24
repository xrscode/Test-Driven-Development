def bubble_sort(ls):
    if not isinstance(ls, list):
        raise TypeError('List required!')
    elif len(ls) == 0:
        raise ValueError('List must be populated!')
    elif not all(isinstance(value, int) for value in ls):
        raise ValueError('Values must be type integer!')
    switch = 1
    while switch != 0:
        switch = 0
        for index, char in enumerate(ls):
            if index == len(ls) - 1:
                continue
            elif char > ls[index + 1]:
                ls[index] = ls[index + 1]
                ls[index + 1] = char
                switch = 1
    return ls
