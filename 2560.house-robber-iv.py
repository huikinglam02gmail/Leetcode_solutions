#
# @lc app=leetcode id=2560 lang=python3
#
# [2560] House Robber IV
#

# @lc code=start
from typing import List


class Solution:
    def Rob(self, cap):
        result = 0
        ind = 0
        while ind < len(self.nums):
            if self.nums[ind] <= cap:
                result += 1
                ind += 2
            else: ind += 1
        return result

    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        self.nums = nums
        while l < r:
            mid = l + (r -  l) // 2
            if self.Rob(mid) >= k: r = mid
            else: l = mid + 1
        return l
        
# @lc code=end

