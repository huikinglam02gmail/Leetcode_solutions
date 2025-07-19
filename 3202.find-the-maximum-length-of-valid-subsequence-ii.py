#
# @lc app=leetcode id=3202 lang=python3
#
# [3202] Find the Maximum Length of Valid Subsequence II
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][j] = length of longest valid subsequence that the last two elements e1 and e2 have e1 % k = i and e2 % k = j
    Given by the condition, (e1 + e2) % k = (e2 + e3) % k. so e1 % k == e3 % k
    '''
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for i in range(k)] for j in range(k)]
        result = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                result = max(result, dp[prev][num])
        return result 


# @lc code=end

