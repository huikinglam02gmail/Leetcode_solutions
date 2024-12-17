#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#

# @lc code=start
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        S = sum(nums)
        for curr in range(len(nums)):
            if nums[curr] == 0:
                for initialDir in range(1, -2, -2):
                    j = curr
                    dir = initialDir
                    arr = nums.copy()
                    currentS = S
                    while 0 <= j < len(arr) and currentS > 0:
                        if arr[j] > 0: 
                            arr[j] -= 1
                            dir = -dir
                            currentS -= 1
                        j += dir
                    if currentS == 0: result += 1
        return result
                    

# @lc code=end

