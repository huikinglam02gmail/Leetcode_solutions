#
# @lc app=leetcode id=3759 lang=python3
#
# [3759] Count Elements With at Least K Greater Values
#

# @lc code=start
from bisect import bisect_right
from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for num in nums:
            if n - bisect_right(nums, num) >= k:
                result += 1
        return result
# @lc code=end

