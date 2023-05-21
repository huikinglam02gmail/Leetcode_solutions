#
# @lc app=leetcode id=1719 lang=python3
#
# [1719] Number Of Ways To Reconstruct A Tree
#

# @lc code=start
from typing import List


class Solution:
    '''
    First construct the graph by linking up the node pairs
    Then nodes with highest degree are the most likely to be root
    So we go from the highest degree nodes and save into visited
    For a node, its parent must be inside visited, and should be the minimum size one that shares the same neighbour as itself.
    if its parent does not exist, and len(graph[x]) is not len(graph) - 1, we can return 0
    If its parent does exist, we ask if graph[x] is a subset of {graph[p] | p}. If not, we can return 0
    Else we ask if graph[x] has same size as graph[p]
    '''
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = {}
        for x, y in pairs:
            if x not in graph:
                graph[x] = set()
            if y not in graph:
                graph[y] = set()
            graph[x].add(y)
            graph[y].add(x)
        
        visited = set()
        multiple = False
        for x in sorted(graph.keys(), key = lambda y: - len(graph[y])):
            p = min(graph[x] & visited, key = lambda y: len(graph[y]), default=0)
            visited.add(x)
            if p > 0:
                if not graph[x].issubset(graph[p] | {p}):
                    return 0
                multiple |= len(graph[x]) == len(graph[p])
            elif len(graph[x]) != len(graph) - 1:
                return 0
        return 1 + (1 if multiple else 0)
# @lc code=end

