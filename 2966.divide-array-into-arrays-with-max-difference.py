#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result, n = [], len(nums)
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k: return []
            else: result.append([nums[i], nums[i + 1], nums[i + 2]])
        return result
# @lc code=end

