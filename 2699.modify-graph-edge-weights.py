#
# @lc app=leetcode id=2699 lang=python3
#
# [2699] Modify Graph Edge Weights
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Break down the problem, what condition will be impossible?
    1. If all mutable edges are ignored, and minimum cost from source to destination < target
    2. If all mutable edges are set to 1, and minimum cost from source to destination > target
    If it's possible, then there exist 1 or more mutable edges (u, v) in which minDist(src, dest) = dist < target if all mutable edge weights are set to 1.
    Set the first mutable edge weight along its path to target to 1 + target - minDist. Dijkstra again with the new graph until dist == target
    '''
    
    '''
    graph is supposed to be [{} for i in range(n)], with graph[i][j] = weight[i][j]
    return [SSP weight from source to ith node] + [SSP path from source to ith node]
    O(n^2 log(n)) time
    '''
    def Dijkstra(self, graph, source, destination):
        n = len(graph)
        result = [[-1] for i in range(n)]
        heap = []
        heapq.heappush(heap, [0, source])
        result[source] = [0, source]
        
        while heap:
            data = heapq.heappop(heap)
            if data[-1] == destination: break
            if data[0] == result[data[-1]][0]:
                for nxt in graph[data[-1]].keys():
                    nxtExtraWeight = graph[data[-1]][nxt]
                    if result[nxt][0] < 0 or result[nxt][0] > data[0] + nxtExtraWeight:
                        data[0] += nxtExtraWeight
                        data.append(nxt)
                        result[nxt] = data.copy()
                        heapq.heappush(heap, data.copy())
                        data[0] -= nxtExtraWeight
                        data.pop()        
        return result[destination]


    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = [{} for i in range(n)]
        for u, v, w in edges:
            if w != -1:
                graph[u][v] = w
                graph[v][u] = w

        SSP = self.Dijkstra(graph, source, destination)
        if -1 < SSP[0] < target: return []

        mutables = [{} for i in range(n)]
        for i, [u, v, w] in enumerate(edges):
            if w == -1:
                mutables[u][v] = i
                mutables[v][u] = i
                edges[i][2] = 1
                graph[u][v] = 1
                graph[v][u] = 1

        SSP = self.Dijkstra(graph, source, destination)
        if SSP[0] > - 1 and SSP[0] > target: return []

        while SSP[0] < target:
            for i in range(1, len(SSP) - 1):
                if SSP[i + 1] in mutables[SSP[i]] and edges[mutables[SSP[i]][SSP[i + 1]]][2] == 1:
                    edges[mutables[SSP[i]][SSP[i + 1]]][2] = target - SSP[0] + 1
                    mutables[SSP[i]].pop(SSP[i + 1])
                    mutables[SSP[i + 1]].pop(SSP[i])
                    graph[SSP[i]][SSP[i + 1]] = target - SSP[0] + 1
                    graph[SSP[i + 1]][SSP[i]] = target - SSP[0] + 1
                    break
            SSP = self.Dijkstra(graph, source, destination)
        return edges

        
# @lc code=end

