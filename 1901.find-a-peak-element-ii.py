#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Similar idea to Leetcode 162.
    to achieve min(m, n) log (max(m, n)) time, choose a mid row / column and find its max element
    if its neighboring elements are smaller than itself, we can return the current element
    else, search the side in which it has larger element.
    '''

    def getMaxRow(self, mat, col):
        row = 0
        current = - 1
        for i in range(len(mat)):
            if mat[i][col] > current:
                current = mat[i][col]
                row = i
        return row

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        if m > n:
            result = self.findPeakGrid([[mat[i][j] for i in range(m)] for j in range(n)])
            return [result[1], result[0]]
        elif n == 1:
            return [0, 0]
        else:
            l, r = 0, n
            while l < r:
                mid = l + (r - l) // 2
                row = self.getMaxRow(mat, mid)
                if (mid == 0 or mat[row][mid - 1] < mat[row][mid]) and (mid == n - 1 or mat[row][mid + 1] < mat[row][mid]):
                    return [row, mid]
                elif mid > 0 and mat[row][mid - 1] > mat[row][mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return [self.getMaxRow(mat, l), l]


# @lc code=end

