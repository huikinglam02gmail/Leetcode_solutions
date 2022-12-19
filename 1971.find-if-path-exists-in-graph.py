#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # Just BFS
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        dq = deque()
        visited = set()
        dq.append(source)
        visited.add(source)
        while dq:
            node = dq.popleft()
            if node == destination:
                return True
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    dq.append(nxt)
        return False
# @lc code=end

