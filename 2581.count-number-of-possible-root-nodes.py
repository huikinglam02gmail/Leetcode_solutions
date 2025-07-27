#
# @lc app=leetcode id=2581 lang=python3
#
# [2581] Count Number of Possible Root Nodes
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        self.graph = [set() for _ in range(len(edges) + 1)]
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
        
        self.guessMap = [set() for _ in range(len(edges) + 1)]
        for a, b in guesses: self.guessMap[a].add(b)
        result = [0] * (len(edges) + 1)
        self.subTreeCounts = [[0, 0] for i in range(len(edges) + 1)]
        self.dfs(0, -1)
        dq = deque()
        dq.append([0, -1, self.subTreeCounts[0][0], self.subTreeCounts[0][1]])
        while dq:
            node, parent, subTreeTrue, subTreeFalse = dq.popleft()
            result[node] = subTreeTrue
            for nxt in self.graph[node]:
                if nxt == parent: continue
                nxtTrue = subTreeTrue
                nxtFalse = subTreeFalse
                if nxt in self.guessMap[node]: 
                    nxtFalse += 1
                    nxtTrue -= 1
                if node in self.guessMap[nxt]: 
                    nxtTrue += 1
                    nxtFalse -= 1
                dq.append([nxt, node, nxtTrue, nxtFalse])
        return [result[i] >= k for i in range(len(edges) + 1)].count(True)


    def dfs(self, node: int, parent: int):
        for nxt in self.graph[node]:
            if nxt == parent: continue
            if nxt in self.guessMap[node]: self.subTreeCounts[node][0] += 1
            if node in self.guessMap[nxt]: self.subTreeCounts[node][1] += 1
            self.dfs(nxt, node)
            self.subTreeCounts[node][0] += self.subTreeCounts[nxt][0]
            self.subTreeCounts[node][1] += self.subTreeCounts[nxt][1]

# @lc code=end

