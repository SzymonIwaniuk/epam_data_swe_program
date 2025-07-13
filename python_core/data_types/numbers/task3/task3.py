from typing import List


def foo(nums: List[int]) -> List[int]:
    produckt = 1
    n = len(nums)

    for multi in nums:
        produckt *= multi

    for i in range(n):
        nums[i] = produckt // nums[i]

    return nums

