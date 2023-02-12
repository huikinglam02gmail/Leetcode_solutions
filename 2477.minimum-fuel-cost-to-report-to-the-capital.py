#
# @lc app=leetcode id=2477 lang=python3
#
# [2477] Minimum Fuel Cost to Report to the Capital
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    # Do a DFS
    # record subtree size
    def dfs(self, node, parent):
        count = 1
        for nxt in self.graph[node]:
            if nxt != parent:
                childCount = self.dfs(nxt, node)
                self.result += - (childCount // - self.seats)
                count += childCount
        return count

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.result = 0
        self.seats = seats
        n = len(roads) + 1
        self.graph = [set() for i in range(n)]
        for a, b in roads:
            self.graph[a].add(b)
            self.graph[b].add(a)
        
        self.dfs(0, -1)
        return self.result

                            
# @lc code=end

