#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
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
    First BFS from 0 to find the total weight from 0 to each node.
    Given each pair of nodes (a, b), the weight of the path from a to b (weight[a, b]) = weight[a] + weight[b] - 2 * weight[lca(a,b)].
    And for 3 nodes (a, b, c), the minimum total weight of a subtree such that it is possible to reach a from both b and c using edges in this subtree = (weight[a, b] + weight[b, c] + weight[c, a]) // 2
    We will use Tarjan's offline LCA algorithm to find all the LCA of each query.
    '''
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [{} for _ in range(len(edges) + 1)]
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        dq = deque()
        dq.append(0)
        visited = [False] * (len(edges) + 1)
        visited[0] = True
        weight = [0] * (len(edges) + 1)
        while dq:
            u = dq.popleft()
            for v, w in graph[u].items():
                if not visited[v]:
                    visited[v] = True
                    weight[v] = weight[u] + w
                    dq.append(v)
        
        pairs = [set() for _ in range(len(edges) + 1)]
        for a, b, c in queries:
            pairs[a].add(b)
            pairs[a].add(c)
            pairs[b].add(a)
            pairs[b].add(c)
            pairs[c].add(a)
            pairs[c].add(b)
        
        lcaMap = self.tarjan_lca(graph, pairs)
        result = []
        for a, b, c in queries:
            result.append(weight[a] + weight[b] + weight[c] - weight[lcaMap[tuple(sorted((a, b)))]] - weight[lcaMap[tuple(sorted((b, c)))]] - weight[lcaMap[tuple(sorted((c, a)))]])
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

