#
# @lc app=leetcode id=2513 lang=python3
#
# [2513] Minimize the Maximum of Two Arrays
#

# @lc code=start
from math import lcm


class Solution:
    '''
    We use binary search to find the answer. Suppose the ans is x
    1. In arr1, # of elements smaller than and indivisible by divisor1 = x - x // divisor1. We require x - x // divisor1 >= uniqueCnt1
    2. In arr2, # of elements smaller than and indivisible by divisor2 = x - x // divisor2. We require x - x // divisor2 >= uniqueCnt2
    3. For the third condition, we must skip multiples of lcm in both arr1 and arr2: x - x // lcm(divisor1, divisor2) >= uniqueCnt1 + uniqueCnt2
    '''
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r, LCM = 0, 10000000000, lcm(divisor1, divisor2)
        while l < r:
            m = l + (r - l) // 2
            if m - m // divisor1 >= uniqueCnt1 and m - m // divisor2 >= uniqueCnt2 and m - m // LCM >= uniqueCnt1 + uniqueCnt2: r = m
            else: l = m + 1
        return l
# @lc code=end

