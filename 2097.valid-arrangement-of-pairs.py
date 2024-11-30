#
# @lc app=leetcode id=2097 lang=python3
#
# [2097] Valid Arrangement of Pairs
#

# @lc code=start
from typing import List


class Solution:
    '''
    Hieholzer's algorithm
    '''
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = {}
        degree = {}
        for a, b in pairs:
            if a not in graph: graph[a] = []
            graph[a].append(b)
            degree[a] = degree.get(a, 0) + 1
            degree[b] = degree.get(b, 0) - 1
        
        start = -1 
        for x in graph.keys():
            start = x
            if degree[x] == 1: break
        
        stack = []
        stack.append(start)
        ans = []
        while stack:
            while stack[-1] in graph and graph[stack[-1]]: stack.append(graph[stack[-1]].pop())
            ans.append(stack.pop())
        return [[ans[i], ans[i - 1]] for i in range(len(ans) - 1, 0, -1)]
# @lc code=end

