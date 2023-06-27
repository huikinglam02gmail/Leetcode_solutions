#
# @lc app=leetcode id=1782 lang=python3
#
# [1782] Count Pairs Of Nodes
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= queries.length <= 20
    2 <= n <= 2 * 10^4
    1 <= edges.length <= 10^5
    For each node, we can find out the degree it get involved in forming an edge
    Then for a < b, incident(a, b) = degree(a) + degree(b) - occurrence of (a, b)
    We need to prepare the sorted array 
    '''
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        
# @lc code=end

