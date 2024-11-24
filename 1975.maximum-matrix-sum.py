#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    The idea is how many negative is left behind for the final sum.
    If we have a 0 in the matrix, we can flip all the negatives to be next to the 0. And the answer is sum (abs(matrix[i][j]))
    If we have even numbers of negatives in the matrix, we can pairwise flip them next to each other and get all positive
    If we have odd number of negatives, then we must have one negative left behind. Assign it to be the element with minimum absolute value
    '''
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        S, zeros, negs, minAbsSoFar = 0, 0, 0, float("inf")
        for i in range(m):
            for j in range(n):
                S += abs(matrix[i][j])
                if matrix[i][j] == 0: zeros += 1
                elif matrix[i][j] < 0: negs += 1
                minAbsSoFar = min(minAbsSoFar, abs(matrix[i][j]))
        return S if (zeros > 0 or negs % 2 == 0) else S - 2 * minAbsSoFar
        
# @lc code=end

