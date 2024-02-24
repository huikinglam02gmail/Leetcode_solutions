#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
from collections import deque
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            pMax, pMin = max(pu,pv), min(pu,pv)
            self.parents[pMax] = pMin
            self.count -= 1

class Solution:
    '''
    Add [0, firstPerson, 0] to meetings, sort meetings by time.
    For each time, we first build a graph of connections within the same time
    we collect all the people's parent. If any of them has 0 as parent (knows the secret), we bfs from them and union any of its connection.
    '''
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = [[0, firstPerson, 0]] + meetings
        meetings.sort(key = lambda x: x[2])
        
        UF = UnionFindSet(n + 1)
        i = 0
        t = 0
        while i < len(meetings):
            t = meetings[i][2]
            graph = {}
            dq = deque()
            visited = set()
            while i < len(meetings) and t == meetings[i][2]:
                u, v, t = meetings[i]
                if u not in graph: graph[u] = set()
                if v not in graph: graph[v] = set()
                graph[u].add(v)
                graph[v].add(u)
                if UF.find(u) == 0 and u not in visited: 
                    dq.append(u)
                    visited.add(u)
                if UF.find(v) == 0 and v not in visited: 
                    dq.append(v)
                    visited.add(v)
                i += 1
            while dq:
                node = dq.popleft()
                for nxt in graph[node]:
                    if nxt not in visited:
                        if UF.find(nxt) > 0:
                            UF.union(0, nxt)
                        dq.append(nxt)
                        visited.add(nxt)
        result = []
        for i in range(n + 1):
            if UF.find(i) == 0: result.append(i)
        return result
# @lc code=end

