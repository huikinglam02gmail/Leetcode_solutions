#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#

# @lc code=start
from typing import List


class Solution:
    '''
    Compute degree of each node
    Then for each pair, computer deg1 + deg2  (- 1 if they are linked)    
    '''
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0]*n
        for node1, node2 in roads:
            degrees[node1] += 1
            degrees[node2] += 1
        result, roads_set = 0, set()
        for road in roads:
            roads_set.add(tuple(road))
        for node1 in range(n-1):
            for node2 in range(node1 + 1, n):
                if (node1, node2) in roads_set or (node2, node1) in roads_set:
                    result = max(result, degrees[node1] + degrees[node2] - 1)
                else:
                    result = max(result, degrees[node1] + degrees[node2])
        return result
# @lc code=end

