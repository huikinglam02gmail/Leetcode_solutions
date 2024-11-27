#
# @lc app=leetcode id=3243 lang=python3
#
# [3243] Shortest Distance After Road Addition Queries I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [set() for i in range(n)]
        for i in range(n - 1): graph[i].add(i + 1)
        result = []
        for q1, q2 in queries:
            graph[q1].add(q2)
            steps = 0
            dq = deque()
            dq.append(0)
            visited = [False] * n
            visited[0] = True
            reached = False
            while dq:
                for i in range(len(dq)):
                    node = dq.popleft()
                    if node == n - 1 and not reached:
                        result.append(steps)
                        reached = True
                    for nxt in graph[node]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            dq.append(nxt)
                steps += 1
        return result
# @lc code=end

