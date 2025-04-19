#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        arr = []
        for i in range(n): 
            result += bisect.bisect_right(arr, upper - nums[i]) - bisect.bisect_left(arr, lower - nums[i])
            arr.append(nums[i])
        return result

            

# @lc code=end
