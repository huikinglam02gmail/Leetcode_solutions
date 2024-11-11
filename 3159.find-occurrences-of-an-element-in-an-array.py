#
# @lc app=leetcode id=3159 lang=python3
#
# [3159] Find Occurrences of an Element in an Array
#

# @lc code=start
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrence = []
        for i, num in enumerate(nums):
            if num == x: occurrence.append(i)
        for i, query in enumerate(queries):
            if query - 1 < len(occurrence): queries[i] = occurrence[query - 1]
            else: queries[i] = -1
        return queries
# @lc code=end

