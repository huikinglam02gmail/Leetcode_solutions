#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
import heapq
import math
from typing import List


class Solution:
    '''
    Probability is multiplicative
    Maximum probability = maximum p1*p2*p3*...*pn
    log(P) = log(p1) + log(p2) + log(p3) + ... + log(pn)
    So if we use -log(p) as weight, We can apply Dijkstra to solve the problem    
    '''
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [set() for i in range(n)]
        cost = [float('inf')]*n
        for i, edge in enumerate(edges):
            a, b = edge[0], edge[1]
            if succProb[i] == 0: w = float('inf')
            else: w = - math.log(succProb[i])
            graph[a].add((b, w))
            graph[b].add((a, w))
        
        heap, p = [], 0
        heapq.heappush(heap, [p, start])
        cost[start] = 0
        while heap:
            P, node = heapq.heappop(heap)
            if node == end: return math.exp(-P)
            for nxt, w in graph[node]:
                if P + w < cost[nxt]:
                    heapq.heappush(heap, [P + w, nxt])
                    cost[nxt] = P + w
        return 0
# @lc code=end

