#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0
        for i in range(2, len(nums), 1):
            if 2 * (nums[i - 2] + nums[i]) == nums[i - 1]: result += 1
        return result
# @lc code=end

