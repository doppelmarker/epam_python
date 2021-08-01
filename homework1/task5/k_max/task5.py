"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    list_without_duplicates = set(nums)
    sorted_set = sorted(list_without_duplicates, reverse=True)
    sum_of_elements = 0
    for i in range(k):
        sum_of_elements += sorted_set[i]
    return sum_of_elements
