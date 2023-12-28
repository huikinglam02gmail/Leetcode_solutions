#
# @lc app=leetcode id=2039 lang=python3
#
# [2039] The Time When the Network Becomes Idle
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    There are two key parameters in here: distance of a data server to master and the patience
    The time we are interested in is the time when the last message sent be a data server is received by itself.
    The last message is sent out at t = ((dist[i] - 1) // patience[i]) * patience[i]
    '''
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        dist = [-1] * n
        visited = [False] * n
        graph =  [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        dq = deque()
        dq.append(0)
        visited[0] = True
        steps = 0
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                dist[node] = steps
                for nxt in graph[node]:
                    if not visited[nxt]:
                        dq.append(nxt)
                        visited[nxt] = True
            steps += 2
        
        result = 0
        for i in range(1, n):
            lastOut = ((dist[i] - 1) // patience[i]) * patience[i]
            result = max(result, dist[i] + 1 + lastOut)
        return result
# @lc code=end

