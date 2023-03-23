#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    if number of cables is below n-1, return -1. For the rest, we do not need to concern ourselves with which cable to switch. We just need to return the number of connected components -1     
    '''
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph = [set() for i in range(n)]
        for connection in connections:
            graph[connection[0]].add(connection[1])
            graph[connection[1]].add(connection[0])
        visited = [False for i in range(n)]
        dq = deque()
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dq.append(i)
                visited[i] = True
                count += 1
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if not visited[nxt]:
                            dq.append(nxt)
                            visited[nxt] = True
        return count - 1
# @lc code=end

