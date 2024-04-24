def digital_root(num):
    """
    ARGS:
    Integer

    RETURNS:
    Recursively returns digital root of number.
    """

    if isinstance(num, bool) or not isinstance(num, int):
        raise TypeError(f"""Value is of type: {
                        type(num)} only integers accepted!""")

    if len(str(num)) == 1:
        return num
    else:
        ls = list(str(num))
        number_ls = [int(x) for x in ls]
        total = sum(number_ls)

        if len(str(total)) > 1:
            return digital_root(total)
        else:
            return total
