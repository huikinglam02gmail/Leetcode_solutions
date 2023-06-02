#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Build the graph first, then BFS from every bomb and find how many it can reach
    '''
    def bfslargestClusterSize(self, graph: List[set]):
        n = len(graph)
        result = 0
        for i in range(n):
            dq = deque()
            local = set()
            dq.append(i)
            local.add(i)
            while dq:
                node = dq.popleft()
                for nxt in graph[node]:
                    if nxt not in local:
                        local.add(nxt)
                        dq.append(nxt)
            result = max(result, len(local))
        return result

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [set() for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                distX, distY = bombs[i][0] - bombs[j][0], bombs[i][1] - bombs[j][1]
                if distX * distX + distY * distY <= bombs[i][2] * bombs[i][2]:
                    graph[i].add(j)
                if distX * distX + distY * distY <= bombs[j][2] * bombs[j][2]:
                    graph[j].add(i)
        return self.bfslargestClusterSize(graph)
# @lc code=end

