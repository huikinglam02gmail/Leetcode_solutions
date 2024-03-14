#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(S):
            if S < 0: return 0
            res = i = 0
            for j in range(len(nums)):
                S -= nums[j]
                while S < 0:
                    S += nums[i]
                    i += 1
                res += j - i + 1
            return res
        return atMost(goal) - atMost(goal - 1)
# @lc code=end

