#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from typing import List


class Solution:
    '''
    There can only be up to two possible roots. Just bfs from leaves until only <= 2 nodes remaining 
    '''
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        elif len(edges) == 1:
            return [0, 1]
        else:
            neighbors = [set() for i in range(n)]
            for edge in edges:
                neighbors[edge[0]].add(edge[1])
                neighbors[edge[1]].add(edge[0])
            leaves = []
            for i in range(n):
                if len(neighbors[i]) == 1: leaves.append(i)
            remaining = n
            while remaining > 2:
                new_leaves = []
                while leaves:
                    leaf = leaves.pop()
                    neighbor = neighbors[leaf].pop() # simply connected, only 1 neighbour left
                    remaining -= 1
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1: new_leaves.append(neighbor)
                leaves = new_leaves
            return leaves
# @lc code=end

