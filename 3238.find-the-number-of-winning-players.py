#
# @lc app=leetcode id=3238 lang=python3
#
# [3238] Find the Number of Winning Players
#

# @lc code=start
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts = [[0 for j in range(11)] for i in range(n)]
        for x, y in pick: counts[x][y] += 1
        result = 0
        for i in range(n):
            for j in range(11):
                if counts[i][j] > i: 
                    result += 1
                    break
        return result


# @lc code=end

