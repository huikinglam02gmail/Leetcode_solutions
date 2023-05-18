#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
from typing import List


class Solution:
    '''
    Add indices not in destination
    Or, remove indices in destination    
    '''

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set([i for i in range(n)])
        for x, y in edges:
            if y in result:
                result.remove(y)
        return list(result)
# @lc code=end

