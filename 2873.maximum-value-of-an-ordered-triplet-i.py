#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        slDiff = SortedList()
        slNum = SortedList()
        result = 0
        for i, num in enumerate(nums):
            if len(slDiff) > 0: result = max(result, num * slDiff[-1])
            if len(slNum) > 0: slDiff.add(slNum[-1] - num)
            slNum.add(num)
        return result
            
# @lc code=end

