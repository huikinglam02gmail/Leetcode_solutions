#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for i in range(len(nums)-1):
            if direction == 0:
                if nums[i + 1] > nums[i]:
                    direction = 1
                elif nums[i + 1] < nums[i]:
                    direction = -1
            else:
                if nums[i + 1] > nums[i] and direction != 1:
                    return False
                elif nums[i + 1] < nums[i] and direction != -1:
                    return False
        return True
# @lc code=end

