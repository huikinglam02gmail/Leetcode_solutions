#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sum the rows, Sort    
    '''

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [y[1] for y in sorted([[sum(x), i] for i, x in enumerate(mat)])][:k]
# @lc code=end

