import random
import math

# Non Recursive:
# def binary_search(l, n):
#     # Convert to dictionary list with tuples:
#     dictionary_list = [(index, number) for index, number in enumerate(l)]

#     # Error handling:
#     if n > l[-1]:
#         raise TypeError("Value too large.")
#     elif n < l[0]:
#         raise TypeError("Value too small.")
#     elif isinstance(n, int) == False:
#         raise TypeError("Value must be an integer.")

#     # While loop to reduce list size to 2.
#     while len(dictionary_list) > 2:
#         odd_even = len(dictionary_list) % 2
#         if odd_even == 1:
#             half = int(math.floor(len(dictionary_list)/2))
#         elif len(dictionary_list) > 2 and odd_even == 0:
#             half = int(len(dictionary_list)/2)
#         if dictionary_list[half][1] == n:
#             return dictionary_list[half][0]
#         elif dictionary_list[half][1] > n:
#             dictionary_list = dictionary_list[0:half]
#         elif dictionary_list[half][1] < n:
#             dictionary_list = dictionary_list[half:]

#     # Determine which is correct value:
#     if dictionary_list[0][1] == n:
#         return dictionary_list[0][0]
#     else:
#         return dictionary_list[1][0]

# Recursion:


def binary_search_recursion(l, n, x=0):
    # Convert to LIST to dictionary of tuples if list and not list of tuples:
    if x == 0:
        dictionary_list = [(index, number) for index, number in enumerate(l)]
    else:
        dictionary_list = l
    odd_even_length = len(dictionary_list) % 2

    if odd_even_length:
        # ODD LENGTH LIST
        mid = int(math.floor(len(dictionary_list)/2))
        if dictionary_list[mid][1] < n:
            new_list = dictionary_list[mid:]
            return binary_search_recursion(new_list, n, 1)
        elif dictionary_list[mid][1] > n:
            new_list = dictionary_list[0:mid]
            return binary_search_recursion(new_list, n, 1)
        elif dictionary_list[mid][1] == n:
            return dictionary_list[mid][0]
    else:
        # EVEN LENGTH LIST
        mid = int(len(dictionary_list)/2)
        if dictionary_list[mid][1] < n:
            new_list = dictionary_list[mid:]
            return binary_search_recursion(new_list, n, 1)
        elif dictionary_list[mid][1] > n:
            new_list = dictionary_list[0:mid]
            return binary_search_recursion(new_list, n, 1)
        elif dictionary_list[mid][1] == n:
            return dictionary_list[mid][0]
