#
# @lc app=leetcode id=3468 lang=python3
#
# [3468] Find the Number of Copy Arrays
#

# @lc code=start
from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        candidates = bounds[0]
        for i in range(1, len(original)):
            candidates = [
                max(candidates[0] + original[i] - original[i - 1], bounds[i][0]),
                min(candidates[1] + original[i] - original[i - 1], bounds[i][1])
            ]
            if candidates[0] > candidates[1]: return 0
        return candidates[1] - candidates[0] + 1
            
# @lc code=end

