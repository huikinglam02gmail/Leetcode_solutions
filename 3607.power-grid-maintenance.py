#
# @lc app=leetcode id=3607 lang=python3
#
# [3607] Power Grid Maintenance
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [set() for i in range(c)]
        for u, v in connections:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)
        groups = []
        reverseGroups = [-1 for i in range(c)]
        groupCount = 0
        for i in range(c):
            if reverseGroups[i] == -1:
                groups.append([])
                dq = deque()
                dq.append(i)
                reverseGroups[i] = groupCount
                heapq.heappush(groups[-1], i)
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if reverseGroups[nxt] == -1:
                            reverseGroups[nxt] = groupCount
                            dq.append(nxt)
                            heapq.heappush(groups[-1], nxt)
                groupCount += 1
        
        Inactive = [False for _ in range(c)]
        result = []
        for a, b in queries:
            if a == 1:
                if not Inactive[b - 1]: result.append(b)
                elif len(groups[reverseGroups[b - 1]]) > 0: 
                    result.append(groups[reverseGroups[b - 1]][0] + 1)
                else: result.append(-1)                   
            else: 
                Inactive[b - 1] = True
                while groups[reverseGroups[b - 1]] and Inactive[groups[reverseGroups[b - 1]][0]]: heapq.heappop(groups[reverseGroups[b - 1]])
        return result
# @lc code=end

