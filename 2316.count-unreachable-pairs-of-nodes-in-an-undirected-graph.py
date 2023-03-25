#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Get the all the groups and the count. The result is sum(count[i]*(total - count[i])) // 2
    '''
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        groupCounts = []
        visited = [False]*n
        dq = deque()
        for i in range(n):
            if not visited[i]:
                count = 0
                dq.append(i)
                visited[i] = True
                while dq:
                    node = dq.popleft()
                    count += 1
                    for nxt in graph[node]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            dq.append(nxt)
                groupCounts.append(count)
        
        total = sum(groupCounts)
        result = 0
        for count in groupCounts:
            result += count * (total - count)
        return result // 2


        
# @lc code=end

