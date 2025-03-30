#
# @lc app=leetcode id=2440 lang=python3
#
# [2440] Create Components With Same Value
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    The numbers to try are the factors of sum(nums)
    BFS from the leaves and return -1 if total node sum exceed target
    '''
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        ss, n = sum(nums), len(nums)
        self.graph = [set() for i in range(n)]
        self.degree = [0] * n
        self.nums =  nums
        for a, b in edges:
            self.degree[a] += 1
            self.degree[b] += 1
            self.graph[a].add(b)
            self.graph[b].add(a)    
           
        for cand in range(min(nums), ss):
            if ss % cand == 0 and self.bfs(cand):
                return ss // cand - 1
        return 0
    
    def bfs(self, target):
        nums = self.nums.copy()
        degree = self.degree.copy()
        dq = deque()
        for i in range(len(nums)):
            if degree[i] == 1: dq.append(i)
        
        while dq:
            node = dq.popleft()
            degree[node] = 0
            for nxt in self.graph[node]:
                if nums[node] != target: nums[nxt] += nums[node]
                degree[nxt] -= 1
                if degree[nxt] == 0: return nums[nxt] == target
                elif degree[nxt] == 1: dq.append(nxt)
# @lc code=end

