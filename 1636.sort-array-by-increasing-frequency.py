#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        occur = {}
        for num in nums: occur[num] = occur.get(num, 0) + 1
        return sorted(nums, key = lambda x : [occur[x], - x])
# @lc code=end

