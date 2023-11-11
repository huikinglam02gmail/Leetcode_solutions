#
# @lc app=leetcode id=2642 lang=python3
#
# [2642] Design Graph With Shortest Path Calculator
#

# @lc code=start
import heapq
from typing import List


class Graph:
    '''
    Apply Dijkstra
    '''
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [{} for i in range(n)]
        for f, t, c in edges:
            self.graph[f][t] = c

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.Dijkstra(self.graph, node1)[node2]
    '''
    graph is supposed to be [{} for i in range(n)], with graph[i][j] = weight[i][j]
    return the SSP weight for all nodes
    O(n^2 log(n)) time
    '''
    def Dijkstra(self, graph, source):
        n = len(graph)
        result = [-1] * n
        heap = []
        visited = [False]*n
        visitedCount = 0
        heapq.heappush(heap, [0, source])

        while heap and visitedCount < n:
            weight, node = heapq.heappop(heap)
            if result[node] < 0:
                result[node] = weight
                visited[node] = True
                visitedCount += 1
                for nxt in graph[node].keys():
                    heapq.heappush(heap, [weight + graph[node][nxt], nxt])        
        return result

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
# @lc code=end

