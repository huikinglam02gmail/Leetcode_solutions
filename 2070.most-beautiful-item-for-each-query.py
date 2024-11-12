#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort by price, then beauty.
    Also sort query with index
    Then 
    '''
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        Q = []
        for i, q in enumerate(queries): Q.append([q, i])
        Q.sort()
        items.sort()
        result = [0] * len(queries)
        iQ, iItem = 0, 0
        maxSoFar = 0
        for i in range(len(Q)):
            while iItem < len(items) and items[iItem][0] <= Q[i][0]:
                maxSoFar = max(maxSoFar, items[iItem][1])
                iItem += 1
            result[Q[i][1]] = maxSoFar
        return result
# @lc code=end

