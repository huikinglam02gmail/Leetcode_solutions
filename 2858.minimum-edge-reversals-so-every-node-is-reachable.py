#
# @lc app=leetcode id=2858 lang=python3
#
# [2858] Minimum Edge Reversals So Every Node Is Reachable
#

# @lc code=start
from typing import List


class Solution:
    '''
    Reroot the tree.
    First DFS: find number of edges that needs to be reversed, if searching from node 0 as root.
    Second DFS: we know the answer for node 0. for each children child, ans[child] = ans[parent] + 1 if arrow is forward and ans[parent] - 1 if arrow is backward
    '''
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = [{} for i in range(n)]
        for a, b in edges:
            self.graph[a][b] = 1
            self.graph[b][a] = -1
        
        self.result = [0] * n
        self.result[0] = self.dfs1(0, -1)
        self.dfs2(0, -1)
        return self.result

    def dfs1(self, node, prev):
        result = 0
        for nxt in self.graph[node]:
            if nxt != prev:
                if self.graph[node][nxt] == -1: result += 1 + self.dfs1(nxt, node)
                else: result += self.dfs1(nxt, node)
        return result

    def dfs2(self, node, prev):
        for nxt in self.graph[node]:
            if nxt != prev:
                if self.graph[node][nxt] == 1: self.result[nxt] = self.result[node] + 1
                else: self.result[nxt] = self.result[node] - 1
                self.dfs2(nxt, node)
    
# @lc code=end

