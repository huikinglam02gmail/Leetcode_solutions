#
# @lc app=leetcode id=2961 lang=python3
#
# [2961] Double Modular Exponentiation
#

# @lc code=start
from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        n = len(variables)
        result = []
        for i in range(n):
            if pow(pow(variables[i][0], variables[i][1], 10), variables[i][2], variables[i][3]) == target: result.append(i)
        return result
# @lc code=end

