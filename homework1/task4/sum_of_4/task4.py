from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sums = {}
    for i in a:
        for j in b:
            if i + j not in sums:
                sums[i + j] = 1
            else:
                sums[i + j] += 1
    counter = 0
    for i in c:
        for j in d:
            if -1 * (i + j) in sums:
                counter += sums[-1 * (i + j)]
    return counter
