from typing import Callable, Iterable, Iterator


def ft_filter(function: Callable, iterable: Iterable) -> Iterator:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))

"""
list comprehension = create list from loop in one line.
need 'A' for 'STH' if 'CON'
example: [x.upper() for x in words if len(x) > 3]
means -> want all x in words to be X if len > 3
[] == list
() == generator
"""