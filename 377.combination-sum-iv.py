#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Sort nums first
    Then dp[i] = the number of possible combinations that add up to i
    Then dp[i] = add all contributions from nums[j] that dp[i] += dp[i - nums[j]]    
    '''

    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(nums[0],target + 1):
            limit = bisect.bisect_right(nums, i)
            for j in range(limit):
                dp[i] += dp[i - nums[j]]
        return dp[target]
        
# @lc code=end

