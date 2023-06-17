#
# @lc app=leetcode id=1761 lang=python3
#
# [1761] Minimum Degree of a Connected Trio in a Graph
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= n <= 400
    We can find trios by brute force
    First construct the graph. Record the degree of each node
    Then the degree of each trio is degree[u] + degree[v] + degree[w] - 6
    '''
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        degree = [0] * n
        for u, v in edges:
            graph[v - 1].add(u - 1)
            graph[u - 1].add(v - 1)
            degree[u - 1] += 1
            degree[v - 1] += 1
        result = 3 * n
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if j in graph[i] and k in graph[i] and k in graph[j]:
                        result = min(result, degree[i] + degree[j] + degree[k] - 6)
        return result if result != 3 * n else - 1
 # @lc code=end
