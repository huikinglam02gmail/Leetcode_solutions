#
# @lc app=leetcode id=2896 lang=python3
#
# [2896] Apply Operations to Make Two Strings Equal
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    Record all the positions where s1 and s2 differ.
    '''
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        self.diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]: self.diffs.append(i)
        if len(self.diffs) % 2 == 1: return -1
        return self.dfs(0, x) // 2

    @lru_cache(None)
    def dfs(self, start, x):
        if start >= len(self.diffs): return 0
        res = float('inf')
        if start < len(self.diffs) - 1: res = min(res, 2 * (self.diffs[start + 1] - self.diffs[start]) + self.dfs(start + 2, x))
        res = min(res, x + self.dfs(start + 1, x))
        return res

# @lc code=end

