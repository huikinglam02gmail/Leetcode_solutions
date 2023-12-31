#
# @lc app=leetcode id=2045 lang=python3
#
# [2045] Second Minimum Time to Reach Destination
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    We need to know two quantities for each node:
    1. What is the minimum time to reach a node?
    2. What is the second minimum time to reach a node?
    We can use BFS to populate these two dicts. and return dict2[n - 1]
    '''
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        minimumTime = [[float("inf"), float("inf")] for i in range(n)]
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)
        minimumTime[0][0] = 0
        dq = deque()
        dq.append([0, 0])
        while dq:
            node, t = dq.popleft()
            if ((t // change) % 2): t = ((t // change) + 1) * change
            for nxt in graph[node]:
                nxtTime = t + time
                if minimumTime[nxt][0] > nxtTime:
                    minimumTime[nxt][0] = nxtTime
                    dq.append([nxt, nxtTime])
                elif minimumTime[nxt][0] < nxtTime < minimumTime[nxt][1]:
                    minimumTime[nxt][1] = nxtTime
                    dq.append([nxt, nxtTime])
        return minimumTime[-1][1]                   
# @lc code=end

