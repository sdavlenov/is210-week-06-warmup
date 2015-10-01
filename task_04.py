#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 04 docstring"""


def process_data(data):
    """Function that returns sum and average of data.

    Args:
        data(list): numbers

    Returns:
        A tuple that has the sum total and average.

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)

        >>> process_data([10, 25, 43, 56, 68])
        (202, 40.4)

    """
    total = 0
    for i in data:
        total = total+i

    average = total/float(len(data))

    return (total, average)
