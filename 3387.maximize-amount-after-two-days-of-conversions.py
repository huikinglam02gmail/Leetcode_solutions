#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        graph = {}
        for i in range(len(pairs1)):
            if pairs1[i][0] not in graph: graph[pairs1[i][0]] = {}
            if pairs1[i][1] not in graph: graph[pairs1[i][1]] = {}
            graph[pairs1[i][0]][pairs1[i][1]] = rates1[i]
            graph[pairs1[i][1]][pairs1[i][0]] = 1 / rates1[i]
        
        intermediate = {}
        dq = deque()
        visited = set()
        dq.append([initialCurrency, 1])
        visited.add(initialCurrency)
        while dq:
            node, val = dq.popleft()
            intermediate[node] = val
            for nxt in graph[node]:
                if nxt not in visited:
                    dq.append([nxt, val * graph[node][nxt]])
                    visited.add(nxt)

        graph = {}
        for i in range(len(pairs2)):
            if pairs2[i][0] not in graph: graph[pairs2[i][0]] = {}
            if pairs2[i][1] not in graph: graph[pairs2[i][1]] = {}
            graph[pairs2[i][0]][pairs2[i][1]] = rates2[i]
            graph[pairs2[i][1]][pairs2[i][0]] = 1 / rates2[i]
        result = 0

        for key in intermediate.keys():
            dq = deque()
            visited = set()
            dq.append([key, intermediate[key]])
            visited.add(key)
            while dq:
                node, val = dq.popleft()
                if node == initialCurrency: result = max(result, val)
                if node in graph:
                    for nxt in graph[node]:
                        if nxt not in visited:
                            dq.append([nxt, val * graph[node][nxt]])
                            visited.add(nxt)
        return result
# @lc code=end

