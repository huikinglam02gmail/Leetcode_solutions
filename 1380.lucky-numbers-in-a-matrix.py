#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    Loop through the column and rows to look for min in row and max in column    
    '''
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row, max_col, m, n = set(), set(), len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            minsofar, result = float('Inf'), []
            for j, num in enumerate(row):
                if num < minsofar:
                    minsofar = num
                    result = [(i,j)]
                elif num == minsofar:
                    result += [(i,j)]
            for item in result:
                min_row.add(item)
        
        for j in range(n):
            maxsofar, result = -float('Inf'), []
            for i in range(m):    
                num = matrix[i][j]
                if num > maxsofar:
                    maxsofar = num
                    result = [(i,j)]
                elif num == maxsofar:
                    result += [(i,j)]
            for item in result:
                max_col.add(item)
        result = []
        for item in min_row:
            if item in max_col:
                result.append(matrix[item[0]][item[1]])
        return result
# @lc code=end

