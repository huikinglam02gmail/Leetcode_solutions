#
# @lc app=leetcode id=1928 lang=python3
#
# [1928] Minimum Cost to Reach Destination in Time
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    We could Dijkstra from 0 to n - 1, while using the cost as priority. Also we keep track of the time.
    When a certain path has time > maxTime, we just toss the path away.
    Also we only further traverse the path if the current arrival time is smaller than the previous arrival time
    '''

    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for i in range(n)]
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))
        
        pq = []
        arrivals = [float("inf") for i in range(n)]
        heapq.heappush(pq, [passingFees[0], 0, 0])

        while pq:
            cost, node, time = heapq.heappop(pq)
            if time > maxTime:
                continue
            if node == n - 1:
                return cost
            if time < arrivals[node]:
                arrivals[node] = time
                for nxt, dt in graph[node]:
                    heapq.heappush(pq, [passingFees[nxt] + cost, nxt, time + dt ]) 
            
        return -1




# @lc code=end

