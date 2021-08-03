"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
import math
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    element_and_frequency = {}
    for element in inp:
        if element in element_and_frequency:
            element_and_frequency[element] += 1
        else:
            element_and_frequency[element] = 1
    max_freq, min_freq = -math.inf, math.inf
    for key in element_and_frequency.keys():
        freq = element_and_frequency[key]
        if freq < min_freq:
            min_freq = freq
        if freq > max_freq:
            max_freq = freq
    return max_freq, min_freq
