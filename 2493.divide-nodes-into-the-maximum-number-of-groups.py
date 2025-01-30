#
# @lc app=leetcode id=2493 lang=python3
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    First DFS from each node to check if there are not odd-length cycles
    Then BFS from each node within different clusters to find the maximum number of groups    
    '''
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
        
        order = [-1] * n
        clusters = []
        for i in range(n):
            if order[i] < 0:
                stack = []
                stack.append(i)
                order[i] = 0
                clusters.append([i])
                while stack:
                    u = stack.pop()
                    for v in graph[u]:
                        if order[v] < 0:
                            order[v] = order[u] + 1
                            clusters[-1].append(v)
                            stack.append(v)
                        elif order[v] & 1 == order[u] & 1:
                            return -1
        
        groups = 0
        for cluster in clusters:
            result = 0
            for start in cluster:
                dq = deque()
                visited = set()
                dq.append(start)
                visited.add(start)
                group = 0
                while dq:
                    for i in range(len(dq)):
                        node = dq.popleft()
                        for nxt in graph[node]:
                            if nxt not in visited:
                                visited.add(nxt)
                                dq.append(nxt)
                    group += 1
                result = max(result, group)
            groups += result
        
        return groups
        # @lc code=end

