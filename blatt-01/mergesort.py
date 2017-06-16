#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2017, University of Freiburg.
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Leon Gnädinger <leon.gnaedinger@gmail.de>
"""

import time
import sys


def mergeSort(lst):
    """
    Sorts list with mergeSort algorithm. Mutates lst.

    >>> mergeSort([1, 5, 10, 2, 4, 11, 100, 0])
    [0, 1, 2, 4, 5, 10, 11, 100]
    >>> mergeSort([10, 6, 3])
    [3, 6, 10]
    >>> mergeSort([1])
    [1]
    >>> mergeSort([])
    []
    """
    len_lst = len(lst)
    s = 1
    # s grows like 2^n, so we have 1, 2, 4, 8... this is the size of the
    # pieces we want to divide the lists into.
    while s < len_lst:
        m = len_lst - s  # m is the middle of the array where we want to divide
        while m >= 0:
            # use max(m-s, 0) to make sure our left var never gets smaller
            # than 0
            merge(lst, max(m-s, 0), m, m+s)
            m -= s + s
        s += s
    return lst


def merge(lst, left, middle, right):
    """

    Merge two already sorted arrays.
    Modified Hannah Basts function to fit the function
    declarition of .TIP. Mutates lst.

    >>> merge([2, 4, 6, 8, 1, 3, 5, 7], 0, 4, 8)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> merge([1, 2, 3, 4], 0, 4, 4)
    [1, 2, 3, 4]
    >>> merge([1, 2, 3, 4], 0, 0, 4)
    [1, 2, 3, 4]
    >>> merge([], 0, 0, 0)
    []

    """

    result = []
    array1, array2 = lst[left:middle], lst[middle:right]
    n1, n2 = len(array1), len(array2)
    i1, i2 = 0, 0
    while i1 < n1 or i2 < n2:
        if i1 < n1 and (i2 == n2 or array1[i1] <= array2[i2]):
            result.append(array1[i1])
            i1 += 1
        if i2 < n2 and (i1 == n1 or array2[i2] <= array1[i1]):
            result.append(array2[i2])
            i2 += 1

    lst[left:right] = result
    return result


if __name__ == "__main__":
    for n in range(1000, 10001, 1000):
        array = [k for k in range(n, 0, -1)]
        start_time = time.time()
        mergeSort(array)
        end_time = time.time()
        duration_msecs = (end_time - start_time) * 1000
        print("%d\t%d" % (n, duration_msecs))
        sys.stdout.flush()
