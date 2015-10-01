#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 05"""


def flip_keys(to_flip):
    """A function that reverses lists.

    Args:
        to_flip (sequence): The list of items being reversed.

    Returns:
        the original list and the list reversed

    Examples:
        >>> flip_keys([(1, 2, 3), 'a, b, c'])
        [(3, 2, 1), 'c ,b ,a']
    """

    counter = 0
    for value in to_flip:
        to_flip[counter] = value[::-1]
        counter += 1
    return to_flip
