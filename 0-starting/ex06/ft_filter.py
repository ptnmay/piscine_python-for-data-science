"""
ft_filter.py

Custom implementation of the built-in filter() function.

This module defines the ft_filter() function, which returns an iterator
yielding elements from an iterable for which a function returns True.
"""

from typing import Callable, Iterable, Iterator


def ft_filter(function: Callable, iterable: Iterable) -> Iterator:
    """
    Recode of the built-in filter() function using list comprehension.

    Args:
        function (Callable): A function that returns True or False.
        iterable (Iterable): Any iterable object (list, tuple, etc.).

    Returns:
        Iterator: An iterator over the filtered elements.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
