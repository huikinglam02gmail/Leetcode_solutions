#
# @lc app=leetcode id=1605 lang=python3
#
# [1605] Find Valid Matrix Given Row and Column Sums
#

# @lc code=start
from typing import List


class Solution:
    # Since we are looking for nonnegative elements, we are free to insert a lot of zeros
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        result = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]
        return result
        
# @lc code=end

