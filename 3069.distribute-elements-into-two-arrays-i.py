#
# @lc app=leetcode id=3069 lang=python3
#
# [3069] Distribute Elements Into Two Arrays I
#

# @lc code=start
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arrs = [[], []]
        for i in range(n):
            if i < 2: arrs[i].append(nums[i])
            elif arrs[0][-1] > arrs[1][-1]: arrs[0].append(nums[i])
            else: arrs[1].append(nums[i])
        return arrs[0] + arrs[1] 
# @lc code=end

