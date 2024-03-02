#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: x*x)
        return [num*num for num in nums]
# @lc code=end

