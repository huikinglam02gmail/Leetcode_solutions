#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for a, b, distance in roads:
            graph[a-1].add(b-1)
            graph[b-1].add(a-1)
            
        dq = deque()
        visited = set()
        dq.append(0)
        visited.add(0)
        while dq:
            node = dq.popleft()
            for nxt in graph[node]:
                if nxt not in visited:
                    dq.append(nxt)
                    visited.add(nxt)
        
        minsofar = 10000
        for a, b, distance in roads:
            if a - 1 in visited:
                minsofar = min(minsofar, distance)
        return minsofar
# @lc code=end

