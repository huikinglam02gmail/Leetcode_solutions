#
# @lc app=leetcode id=1799 lang=python3
#
# [1799] Maximize Score After N Operations
#

# @lc code=start
from functools import lru_cache
from typing import List

class Solution:
    '''
    1 <= n <= 7, can calculate all possible pairs for gcd
    we can specify the chosen numbers as mask (0 = free, 1 = chosen)
    together with round number specified by i, use dp to solve the problem
    '''
    
    def gcd(self, a, b):
        if (a == 0):
            return b
        else:
            return self.gcd(b % a, a)

    @lru_cache(None)
    def dp(self, mask, round):
        result = 0
        if round <= len(self.nums):
            for i in range(len(self.nums) - 1):
                for j in range(i + 1, len(self.nums), 1):
                    if mask & (1 << i) == 0 and mask & (1 << j) == 0:
                        result = max(result, round * self.gcd(self.nums[i], self.nums[j]) + self.dp(mask ^ (1 << i) ^ (1 << j), round + 1))
        return result

    def maxScore(self, nums: List[int]) -> int:
        self.nums = nums
        return self.dp(0, 1)
# @lc code=end

