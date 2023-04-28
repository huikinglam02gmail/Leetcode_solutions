#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Build graph according to the swap letter condition: hamming distance = 2
    Then BFS from all words to check how many connected components are there    
    '''

    def similar(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if count > 2:
                return False
        return count == 2
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        graph = {}
        for string in strs:
            graph[string] = set()
        
        for i in range(n-1):
            for j in range(i+1, n):
                if self.similar(strs[i], strs[j]):
                    graph[strs[i]].add(strs[j])
                    graph[strs[j]].add(strs[i])
        
        visited = set()
        count = 0
        for string in strs:
            if string not in visited:
                count += 1
                dq = deque()
                dq.append(string)
                visited.add(string)
                while dq:
                    node = dq.popleft()
                    for nxt in graph[node]:
                        if nxt not in visited:
                            dq.append(nxt)
                            visited.add(nxt)
        return count
# @lc code=end

