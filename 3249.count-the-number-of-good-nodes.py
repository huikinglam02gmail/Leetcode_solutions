#
# @lc app=leetcode id=3249 lang=python3
#
# [3249] Count the Number of Good Nodes
#

# @lc code=start
from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        self.graph = [set() for i in range(len(edges) + 1)]
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
        self.result = 0
        totalTreeSize = self.dfs(0, -1)
        return self.result
    
    def dfs(self, node, prev):
        subTreeSizes = set()
        result = 1
        for nxt in self.graph[node]:
            if nxt != prev:
                subtreeSize = self.dfs(nxt, node)
                subTreeSizes.add(subtreeSize)
                result += subtreeSize
        if len(subTreeSizes) <= 1: self.result += 1
        return result
# @lc code=end

