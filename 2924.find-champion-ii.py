#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        degrees = [0] * n
        for u, v in edges:
            graph[v].add(u)
            degrees[u] += 1
        
        dq = deque()
        for i in range(n):
            if degrees[i] == 0:
                dq.append(i)
        
        while dq:
            queueLength = len(dq)
            for i in range(queueLength):
                node = dq.popleft()
                if not graph[node]:
                    if queueLength == 1:
                        return node
                    else:
                        return -1
                else:
                    for j in graph[node]:
                        degrees[j] -= 1
                        if degrees[j] == 0:
                            dq.append(j)
        return -1
# @lc code=end

