#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            if nums[i] == key: indices.append(i)
        result = []
        j = 0
        for i in range(len(nums)):
            while j < len(indices) and indices[j] < i - k: j += 1
            if j < len(indices) and indices[j] <= i + k: result.append(i)
        return result
# @lc code=end

