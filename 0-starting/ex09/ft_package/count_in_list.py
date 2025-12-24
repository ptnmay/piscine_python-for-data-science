"""
count_in_list

This module provides a function to count occurrences
of a value inside a list.
"""


def count_in_list(lst, value):

    """
    count how many times 'value' appears in 'lst'

    Args:
        lst: The List to search in.
        value" the value to count.

    Returns:
        int: number of occurrences of value in the list.
    """
    return lst.count(value)
