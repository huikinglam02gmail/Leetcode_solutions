#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    array nums that consists of n unique elements
    So just count degrees and BFS from one end to another end
    '''
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in adjacentPairs:
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)
        
        for key in graph.keys():
            if len(graph[key]) == 1:
                start = key

        dq = deque()
        visited = set() 
        dq.append(start)
        visited.add(start)
        result = []
        while dq:
            result.append(dq.popleft())
            for nxt in graph[result[-1]]:
                if nxt not in visited:
                    dq.append(nxt)
                    visited.add(nxt)
        return result
# @lc code=end

