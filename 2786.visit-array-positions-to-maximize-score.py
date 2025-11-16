#
# @lc app=leetcode id=2786 lang=python3
#
# [2786] Visit Array Positions to Maximize Score
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[parity] = maximum score we can get when the last number we visit has parity 'parity'.
    The "-x" cost was preincorporated
    In each new number, we only update dp[parity]
    '''
    def maxScore(self, nums: List[int], x: int) -> int:
        dp = [nums[0], nums[0]]
        dp[1 - nums[0] % 2] -= x
        for num in nums[1:]:
            parity = num % 2
            dp[parity] = num + max(dp[parity], dp[1 - parity] - x)
        return max(dp)
# @lc code=end

