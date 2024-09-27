#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS from nodes with 0 adjacency
    '''
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        adj = [0 for i in range(n)]
        ancestors = [set() for i in range(n)]
        dq = deque()
        for f, t in edges: 
            graph[f].append(t)
            adj[t] += 1
            ancestors[t].add(f)
        for i in range(n):
            if not ancestors[i]: dq.append(i)
        while dq:
            node = dq.popleft()
            while graph[node]:
                nxt = graph[node].pop()
                adj[nxt] -= 1
                ancestors[nxt].add(node)
                for ans in ancestors[node]: ancestors[nxt].add(ans)
                if adj[nxt] == 0: dq.append(nxt)
        return [sorted(ans) for ans in ancestors]
# @lc code=end

