#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
from collections import deque
from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.ancestor = list(range(n))

    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j, new_ancestor):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.ancestor[root_i] = new_ancestor

class Solution:
    '''
    Traverse the tree from 1. 
    We need two quantities:
    1. All each query (a, b), find their lowest common ancestor (LCA) in the tree.
    2. The length L  is len(a, lca(a, b)) + len(b, lca(a, b)).
    3. If L = 5, it could be 5 * 1, 2 * 2 + 3 * 1,  4 * 2 + 1 * 1 = 5C5 + 5C3 + 5C1 = 2 ^ (L - 1)
    4. If L = 6, it could be 5 * 1 + 1 * 2, 3 * 1 + 3 * 2, 1 * 1 + 5 * 2 = 6C5 + 6C3 + 6C1 = 2 ^ (L - 1)
    '''
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        pairs = [set() for _ in range(len(edges) + 1)]
        for a, b in queries:
            pairs[a - 1].add(b - 1)
            pairs[b - 1].add(a - 1)
        
        lca_results = self.tarjan_lca(graph, pairs)

        distance = [-1] * (len(edges) + 1)
        dq = deque()
        dq.append(0)
        distance[0] = 0
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    dq.append(v)

        result = []
        for a, b in queries:
            if a == b: result.append(0)
            else:
                a -= 1
                b -= 1
                lca = lca_results[tuple(sorted((a, b)))]
                result.append(pow(2, distance[a] + distance[b] - 2 * distance[lca] - 1, 1000000007))
        return result
    
    def tarjan_lca(self, graph, pairs):
        lca_results = {}
        n = len(graph)
        dsu = DSU(n)
        color = [0] * n

        def dfs(u, parent):
            color[u] = 1
            dsu.ancestor[dsu.find(u)] = u

            for v in graph[u]:
                if v == parent: continue
                if not color[v]:
                    dfs(v, u)
                    dsu.union(u, v, u)

            for v_query in pairs[u]:
                if color[v_query] == 2: lca_results[tuple(sorted((u, v_query)))] = dsu.ancestor[dsu.find(v_query)]

            color[u] = 2
        dfs(0, -1)
        return lca_results  
# @lc code=end

