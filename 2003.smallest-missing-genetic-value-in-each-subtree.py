#
# @lc app=leetcode id=2003 lang=python3
#
# [2003] Smallest Missing Genetic Value in Each Subtree
#

# @lc code=start
from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution:
    '''
    Each nums[i] is distinct, so 1 appears only once.
    Therefore, only the path from root to the node i where nums[i] = 1 has values different from 1.
    From the node with nums[i], we dfs from the node and collect all numbers seen in the current subtree.
    Repeated dfs can be avoided by recording whether a node has been visited before
    '''
    def dfs(self, i):
        if not self.seen[self.nums[i]]:
            self.seen[self.nums[i]] = True
            for c in self.children[i]: self.dfs(c)

    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        result = [1] * n
        self.seen = [False] * 100001
        self.seen[0] = True
        self.children = [[] for i in range(n)]
        self.nums = nums
        
        if 1 in nums:
            miss = 0
            for i, p in enumerate(parents):
                if p != -1: self.children[p].append(i)
                   
            j = nums.index(1)
            while j != -1:
                self.dfs(j)
                while miss < 100001 and self.seen[miss]: miss += 1
                result[j] = miss
                j = parents[j]
        return result
# @lc code=end

