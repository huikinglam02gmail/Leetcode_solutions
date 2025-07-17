#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
import bisect
from collections import deque
from operator import itemgetter
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        edges.sort()
        graph = [{} for _ in range(n)]
        for u, v, s, e in edges: 
            if v not in graph[u]: graph[u][v] = [[-1, -1]]
            if s <= graph[u][v][-1][1] + 1: graph[u][v][-1][1] = e
            else: graph[u][v].append([s, e])
        
        dq = deque()
        dq.append([0, 0])
        minTime = [float('inf')] * n
        minTime[0] = 0
        while dq:
            node, arrivalTime = dq.popleft()
            if minTime[node] < arrivalTime: continue
            for nxt in graph[node]:
                ind = bisect.bisect_left(graph[node][nxt], arrivalTime, key = itemgetter(1))
                if ind < len(graph[node][nxt]) and minTime[nxt] > 1 + max(arrivalTime, graph[node][nxt][ind][0]):
                    minTime[nxt] = 1 + max(arrivalTime, graph[node][nxt][ind][0])
                    dq.append([nxt, minTime[nxt]])
        if minTime[n - 1] != float('inf'):
            return minTime[n - 1]
        else:
            return -1
            
# @lc code=end

