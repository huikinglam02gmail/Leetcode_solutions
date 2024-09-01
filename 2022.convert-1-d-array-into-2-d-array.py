#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m * n == len(original):
            for i in range(m):
                row = []
                for j in range(n):
                    row.append(original[i * n + j])
                result.append(row)
            return result
# @lc code=end

