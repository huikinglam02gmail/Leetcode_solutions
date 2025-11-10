#
# @lc app=leetcode id=3740 lang=python3
#
# [3740] Minimum Distance Between Three Equal Elements I
#

# @lc code=start
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        occur = {}
        for i, num in enumerate(nums):
            if num not in occur: occur[num] = []
            occur[num].append(i)
        result = float('inf')
        for num in occur:
            if len(occur[num]) >= 3:
                for i in range(len(occur[num]) - 2):
                    result = min(result, 2 * (occur[num][i + 2] - occur[num][i]))
        if result == float('inf'):
            return -1
        else:
            return result
# @lc code=end

