#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev = 0
        for num in nums:
            if num != prev: j = 0
            if 0 <= j < len(result):
                result[j].append(num)
            else:
                result.append([num])
            j += 1
            prev = num
        return result
# @lc code=end

