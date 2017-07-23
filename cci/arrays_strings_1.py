#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Filename: arrays_strings_1.py

NOTE if you use this file without using the accompanying book, 
you are missing out on the review of arrays and strings,
plus a lot specific to this question: 
two alternate solutions aside from mine,
discussions of big-O for space,
as well as a few extra "what if" constraints.

So buy the book, it's a good investment!
http://www.crackingthecodinginterview.com/
 
If you already have the book, crack it open and skim this section.
"""


def is_unique(s):
    """Determines if string s has all unique characters. 
    O(n) for time, where n is length of s.
    
    Args:
        s (str): string in question.

    Returns:
        bool: True if all characters are unique, False if some are repeated.
    """
    # Elegant one-liner in Python: return len(s) == len(set(s))
    already_seen = {}
    for char in s:
        if char in already_seen:
            return False
        else:
            already_seen[char] = True
    return True


def is_unique_no_ds(s):
    """Same role as 'is_unique', it determines if a string s has all unique characters.
    However this one does it without any extra data structures at all.
    This one is O(nlogn) for time, since each search (char in minus_char) is logn at best, 
    and we may go through as many as n times.

    Args:
        s (str): string in question.

    Returns:
        bool: True if all characters are unique, False if some are repeated.
    """
    for i, char in enumerate(s):
        minus_char = s[:i] + s[i + 1:]
        if char in minus_char:
            return False
    return True


if __name__ == "__main__":
    test_strings = ['test', 'really', 'nicely', 'Wendy'] 
    functions = [is_unique, is_unique_no_ds]
    for test in test_strings:
        print("Testing '{}'".format(test))
        results = []
        for function in functions: 
            results.append(function(test))
            print("\tResult from '{}': {}".format(function.__name__, results[-1]))
        print("Results from all functions match?: {}".format(len(set(results)) == 1))
        

