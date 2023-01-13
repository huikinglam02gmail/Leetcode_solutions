#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

# @lc code=start
from typing import List


class Solution:
    # Because it's only asking for no same characters between adjacent nodes, then it's rather straightforward
    # We are handling a tree, any paths that passes through a node can be broken down into two paths emanating from the node
    # The idea is similar to Leetcode 543. Diameter of Binary Tree
    # This makes DFSing from 0 (the root) a good strategy.
    # Since the tree is not necessarily binary here, we need to write dfs function to return the set of all maximal path length (that ends at a leaf) emanating from a node to its children
    # These paths contain no adjacent identical characters
    # One important point: we only choose the longest pathlength from its children
    # Then after all the search are done, choose two largest ones and update the global result
    
    def dfs(self, node):
        node_toptwo = [1, 1]
        for i in self.graph[node]:
            children_max_pathlength = self.dfs(i)
            if self.s[i] != self.s[node]:
                newcomer = 1 + children_max_pathlength
                for j in range(2):
                    if newcomer > node_toptwo[j]:
                        node_toptwo[j], newcomer = newcomer, node_toptwo[j]
        self.result = max(self.result, sum(node_toptwo) - 1)
        return node_toptwo[0]
                    
    def longestPath(self, parent: List[int], s: str) -> int:
        # Build the graph
        n = len(parent)
        self.graph = [set() for i in range(n)]
        self.s, self.result = s, 0
        for child, par in enumerate(parent):
            if par >= 0:
                self.graph[par].add(child)
        # DFS
        root_max_pathlength = self.dfs(0)
        return self.result
# @lc code=end

