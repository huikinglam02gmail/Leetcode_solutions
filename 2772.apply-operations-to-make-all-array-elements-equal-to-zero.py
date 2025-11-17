#
# @lc app=leetcode id=2772 lang=python3
#
# [2772] Apply Operations to Make All Array Elements Equal to Zero
#

# @lc code=start
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        cur = 0
        for i in range(len(nums)):
            if cur > nums[i]: return False
            nums[i] -= cur
            cur += nums[i]
            if i >= k - 1: cur -= nums[i - k + 1]
        return cur == 0
# @lc code=end

