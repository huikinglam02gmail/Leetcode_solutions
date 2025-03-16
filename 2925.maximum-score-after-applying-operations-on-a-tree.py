#
# @lc app=leetcode id=2925 lang=python3
#
# [2925] Maximum Score After Applying Operations on a Tree
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    recursive thinking:
    1. get value out a root, and skip one of the nodes in the subtree
    2. skip the root value, and get all the values in the subtree
    dp[i] =  maximum score you can obtain after performing these operations on the tree rooted at i any number of times so that it remains healthy.
    '''
    @lru_cache(None)
    def dp(self, node, parent):
        result = [0, 0]
        for nxt in self.graph[node]:
            if nxt != parent:
                a, b = self.dp(nxt, node)
                result[1] += b
                result[0] += a
        if len(self.graph[node]) > 1 or parent == -1 : result[0] = max(result[0] + self.values[node], result[1])
        result[1] += self.values[node]
        return result
    
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        self.graph = [set() for i in range(len(edges) + 1)]
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
        self.values = values   
        return self.dp(0, -1)[0]
# @lc code=end

