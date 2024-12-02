#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    '''
    Path of bob is fixed (t, i)
    We then BFS Alice from 0 add try to maximize the score until reaches a leaf
    '''
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = [set() for i in range(len(edges) + 1)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        dq = deque()
        dq.append([bob, -1,  [bob]])
        bobArrivalTime = [len(edges) + 1] * (len(edges) + 1)
        arrivedRoot = False
        while dq and not arrivedRoot:
            node, prev, path = dq.popleft()
            if node == 0:
                for j in range(len(path)): bobArrivalTime[path[j]] = j
                arrivedRoot = True
            for nxt in graph[node]:
                if nxt != prev:
                    dq.append([nxt, node, path + [nxt]])
        dq = deque()
        dq.append([0, -1, 0])
        time = 0
        result = - float("inf")
        while dq:
            for i in range(len(dq)):
                node, prev, profit = dq.popleft()
                if time < bobArrivalTime[node]: profit += amount[node]
                elif time == bobArrivalTime[node]:
                    if amount[node] >= 0: profit += (abs(amount[node]) // 2)
                    else: profit -= (abs(amount[node]) // 2)
                if len(graph[node]) == 1 and prev != -1: result = max(result, profit)
                else:
                    for nxt in graph[node]:
                        if nxt != prev: dq.append([nxt, node, profit])
            time += 1
        return result
        


# @lc code=end

