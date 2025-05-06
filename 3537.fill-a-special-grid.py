#
# @lc app=leetcode id=3537 lang=python3
#
# [3537] Fill a Special Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    Divide and conquer
    '''
    def solve(self, startRow, startCol, size, toAdd):
        if size == 1:
            self.ans[startRow][startCol] = toAdd
        else:
            a = size // 2
            self.solve(startRow, startCol, a, toAdd)
            self.solve(startRow + a, startCol, a, toAdd + a * a)
            self.solve(startRow + a, startCol - a , a, toAdd + 2 * a * a)
            self.solve(startRow, startCol - a, a, toAdd + 3 * a * a)

    def specialGrid(self, n: int) -> List[List[int]]:
        self.ans = [[0 for j in range(pow(2, n))] for i in range(pow(2, n))]
        self.solve(0, pow(2, n) - 1, pow(2, n), 0)
        return self.ans
        
# @lc code=end

