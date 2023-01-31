#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq
from typing import List


class Solution:
    # Dijkstra's algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [{} for i in range(n)]
        for time in times:
            graph[time[0] - 1][time[1] - 1] = time[2]
        
        heap = []
        visited = [False]*n
        visitedCount = 0
        heapq.heappush(heap, [0, k - 1])

        while heap and visitedCount < n:
            time, node = heapq.heappop(heap)
            if not visited[node]:
                visited[node] = True
                visitedCount += 1
                for nxt in graph[node].keys():
                    heapq.heappush(heap, [time + graph[node][nxt], nxt])

        if visitedCount < n:
            return -1
        else:
            return time  
            
# @lc code=end
