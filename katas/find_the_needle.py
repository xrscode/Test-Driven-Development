haystack = {
    'name': "Northcoders",
    'description': "Awesome coding bootcamp",
    'staff': {
        'tutors': "James and Chris",
        'support': "Louise"
    },
    'contactDetails': {
        'web': "https://northcoders.com",
        'phone': "",
        'address': {
            'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
            'postcode': "M40 5BJ"
        }
    },
    'reviews': {
        'april': {
            'chris': "I love Northcoders",
            'james': "It is awesome!"
        },
        'may': {
            'louise': "Northcoders is a fantastic coding bootcamp", 'second': {'hi': 'no'}
        }
    }
}


def needle(haystack, needle, path=''):
    for item in haystack:
        if isinstance(haystack[item], dict):
            needle(haystack[item], needle, path + item + '.')
        else:
            if haystack[item] == needle:
                print('Needle found at path:', path + item)
                return  # Exit the function when needle is found

    return path


print(needle(haystack, 'm40', ''))
