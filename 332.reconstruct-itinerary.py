#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    DFS with backtracking
    Make sure sort the tickets first    
    '''
    @lru_cache(None)
    def dfs(self, current, itinerary):
        if all(self.used):
            self.result = itinerary + current
            self.found = True
        elif current in self.graph and self.graph[current]:
            for id, nxt in self.graph[current]:
                if not self.used[id] and not self.found:
                    self.used[id] = True
                    self.dfs(nxt, itinerary + current)
                    self.used[id] = False
                        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = {}
        self.found = False
        tickets.sort()
        for i, ticket in enumerate(tickets):
            if ticket[0] not in self.graph:
                self.graph[ticket[0]] = [[i, ticket[1]]]
            else:
                self.graph[ticket[0]].append([i, ticket[1]])
        
        self.result = ""
        self.used = [False for i in range(len(tickets))]
        self.dfs("JFK", "")
        string_list = []
        i = 0
        while i < len(self.result):
            string_list.append(self.result[i:i+3])
            i += 3
        return string_list
# @lc code=end

