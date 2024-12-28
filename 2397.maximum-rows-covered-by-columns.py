#
# @lc app=leetcode id=2397 lang=python3
#
# [2397] Maximum Rows Covered by Columns
#

# @lc code=start
from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        masks = self.generateKSetBitSetWithTotalLengthN(n, numSelect)
        for mask in masks:
            count = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 1 and (mask & (1 << j)) == 0: 
                        count += 1
                        break
            result = max(result, m - count)
        return result
        
    def generateKSetBitSetWithTotalLengthN(self, N, K):
        result = set()
        cur = (1 << K) - 1
        while cur < (1 << N):
            result.add(cur)            
            lowbit = cur & ~(cur - 1)
            ones = cur & ~(cur + lowbit)
            cur += lowbit + (ones // lowbit // 2)
        return result
# @lc code=end

