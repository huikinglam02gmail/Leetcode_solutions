#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    At a first glance one might thought we should solve this by Dijkstra. But check out the conditions:
    1 <= routes.length <= 500.
    sum(routes[i].length) <= 10^5
    We should instead use routes as nodes. Connect two routes if they intersect
    We finally BFS from routes that contain source
    '''
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        stations = [set() for i in range(n)]
        for i, route in enumerate(routes):
            stations[i] = set(route)
        
        graph =  [set() for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(stations[i] & stations[j]) > 0:
                    graph[i].add(j)
                    graph[j].add(i)

        dq = deque()
        visited = [False] * n
        steps = 1
        for i in range(n):
            if source in stations[i]:
                visited[i] = True
                dq.append(i)
        
        while dq:
            for i in range(len(dq)):
                route = dq.popleft()
                if target in stations[route]:
                    return steps
                for nxt in graph[route]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        dq.append(nxt)
            steps += 1
        return -1
# @lc code=end

