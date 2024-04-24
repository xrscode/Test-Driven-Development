# Get Years of Growth
def get_years_of_growth(start, end, percent, migration):
    if not all(isinstance(arg, int)
               for arg in (start, end, percent, migration)):
        raise TypeError('Only integers accepted!')

    if not start < end:
        raise ValueError('End year can not be less than start year!')

    years = 0

    while start < end:
        years += 1
        start *= 1 + percent / 100
        start += migration
    return years
