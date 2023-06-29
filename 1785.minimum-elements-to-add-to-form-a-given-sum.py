#
# @lc app=leetcode id=1785 lang=python3
#
# [1785] Minimum Elements to Add to Form a Given Sum
#

# @lc code=start
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums) - goal) + limit - 1) // limit
# @lc code=end

