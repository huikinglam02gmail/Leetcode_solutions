#
# @lc app=leetcode id=2718 lang=python3
#
# [2718] Sum of Matrix After Queries
#

# @lc code=start
from typing import List


class Solution:
    '''
    Process queries in reverse order, keep tracking of unseen rows and columns.
    '''
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        result = 0
        unSeenRows = set(range(n))
        unSeenCols = set(range(n))
        for type, index, val in reversed(queries):
            if type == 0 and index in unSeenRows:
                result += val * len(unSeenCols)
                unSeenRows.remove(index)
            elif type == 1 and index in unSeenCols:
                result += val * len(unSeenRows)
                unSeenCols.remove(index)
        return result
# @lc code=end

