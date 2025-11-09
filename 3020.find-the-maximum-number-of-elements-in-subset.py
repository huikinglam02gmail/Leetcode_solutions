#
# @lc app=leetcode id=3020 lang=python3
#
# [3020] Find the Maximum Number of Elements in Subset
#

# @lc code=start
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1
        result = 0
        if 1 in occur:
            if occur[1] % 2 == 1: result = max(result, occur[1])
            else: result = max(result, occur[1] - 1)
        for key in occur:
            if key == 1: continue
            key1 = key
            current = 1
            while key1 in occur:
                if occur[key1] > 1 and key1 * key1 in occur: current += 2
                key1 *= key1
            result = max(result, current)
        return result
# @lc code=end
