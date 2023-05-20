#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Build the graph, with [target, value] as value and start as key
    Then for each query, BFS from start to target
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, equation in enumerate(equations):
            if equation[0] not in graph:
                graph[equation[0]] = set()
            if equation[1] not in graph:            
                graph[equation[1]] = set()
            graph[equation[0]].add((equation[1], values[i]))
            graph[equation[1]].add((equation[0], 1 /values[i]))              

        result = []
        for i, query in enumerate(queries):
            if query[0] in graph and query[1] in graph:
                dq = deque()
                visited = set()
                dq.append((query[0], 1))
                visited.add(query[0])
                while dq:
                    node, res = dq.popleft()
                    if node == query[1]:
                        result.append(res)
                        break
                    for nxt, val in graph[node]:
                        if nxt not in visited:
                            visited.add(nxt)
                            dq.append((nxt, res * val ))
            if len(result) < i + 1:
                result.append(-1)
        return result
# @lc code=end

