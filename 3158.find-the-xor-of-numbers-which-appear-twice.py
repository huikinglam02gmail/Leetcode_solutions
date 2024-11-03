#
# @lc app=leetcode id=3158 lang=python3
#
# [3158] Find the XOR of Numbers Which Appear Twice
#

# @lc code=start
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = [0] * 50
        for num in nums: counts[num - 1] += 1
        result = 0
        for i in range(50):
            if counts[i] == 2: result ^= (i - 1)
        return result        
# @lc code=end

