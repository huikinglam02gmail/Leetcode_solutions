#
# @lc app=leetcode id=1649 lang=python3
#
# [1649] Create Sorted Array through Instructions
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList

class Solution:
    # Use sortedlist to handle the problem
    def createSortedArray(self, instructions: List[int]) -> int:
        s = SortedList()
        result = 0
        MOD = pow(10, 9) + 7
        for i, instruction in enumerate(instructions):
            result += min(s.bisect_left(instruction), i - s.bisect_right(instruction))
            result %= MOD
            s.add(instruction)
        return result
# @lc code=end

