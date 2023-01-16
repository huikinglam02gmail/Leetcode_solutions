#
# @lc app=leetcode id=1617 lang=python3
#
# [1617] Count Subtrees With Max Distance Between Cities
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # 2 <= n <= 15
    # Therefore can use bitmask to represent cities included
    # For each mask, we bfs from one of the nodes
    # if we cannot reach every node, it means the current mask does not represent a valid subset
    # if we pass the test, we bfs from the last member in topologically sorted and get the maximum distance
    
    def bfs(self, mask, start):
        dq = deque()
        visited = []
        dq.append(start)
        visited.append(start)
        steps = 0
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                for nxt in self.graph[node]:
                    if mask & (1 << nxt) != 0 and nxt not in visited:
                        dq.append(nxt)
                        visited.append(nxt)
            if dq:
                steps += 1
        return [steps] + visited

    def setBitCounter(self, mask):
        result = 0
        while mask > 0:
            if mask % 2 == 1:
                result += 1
            mask = mask >> 1
        return result

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = [set() for i in range(n)]
        result = [0]*n
        for a, b in edges:
            self.graph[a - 1].add(b - 1)
            self.graph[b - 1].add(a - 1)
        
        for mask in range(1 << n):
            i = 0
            while (i < n and mask & (1 << i) == 0):
                i += 1
            if i < n:
                bfsResult = self.bfs(mask, i)
                if len(bfsResult) - 1 == self.setBitCounter(mask):
                    lastNode = bfsResult.pop()
                    bfsResultFromEdge = self.bfs(mask, lastNode)
                    result[bfsResultFromEdge[0]] += 1
        return result[1:]

# @lc code=end