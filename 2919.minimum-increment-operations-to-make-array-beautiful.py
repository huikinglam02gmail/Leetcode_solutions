#
# @lc app=leetcode id=2919 lang=python3
#
# [2919] Minimum Increment Operations to Make Array Beautiful
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Use dp. dp[i] = the minimum operations to make nums[:i] beautiful, and nums[i] >= k.
    '''
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = deque()
        for i in range(n):
            dp.append(max(0, k - nums[i]))
            if i >= 3:
                dp[3] += min(dp[0], dp[1], dp[2])
                dp.popleft()
        return min(dp)
# @lc code=end

