from datetime import datetime


def lengthen_date(date):
    # Error handling:
    if not isinstance(date, str):
        raise TypeError('String required!')

    if '/' in date:
        date = date.replace('/', '.')


# Attempt to parse date string:
    try:
        obj = datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        raise ValueError('Must be a valid date!')

# Convert day into integer:
    day = int(datetime.strftime(obj, "%d"))


# Suffix dict:
    suffix = {1: 'st', 2: 'nd', 3: 'rd', 4: 'th',
              5: 'th', 6: 'th', 7: 'th', 8: 'th',
              9: 'th', 10: 'th', 11: 'th', 12: 'th',
              13: 'th', 14: 'th', 15: 'th', 16: 'th',
              17: 'th', 18: 'th', 19: 'th', 20: 'th',
              21: 'st', 22: 'nd', 23: 'rd', 24: 'th',
              25: 'th', 26: 'th', 27: 'th', 28: 'th',
              29: 'th', 30: 'th', 31: 'st'}


# Write date string:
    time_str = datetime.strftime(obj, f"%A %d{suffix[day]} %B %Y")

    return time_str
