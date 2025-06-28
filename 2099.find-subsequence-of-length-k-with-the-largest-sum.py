#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = list(enumerate(nums))
        arr.sort(key = lambda x: x[1])
        idx = [i for i, j in arr[-k:]]
        idx.sort()
        return [nums[i] for i in idx]
# @lc code=end

