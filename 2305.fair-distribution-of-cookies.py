#
# @lc app=leetcode id=2305 lang=python3
#
# [2305] Fair Distribution of Cookies
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    k <= 8, small enough for DFS
    try to give each cookie to ith child, and find out the maximum one owns at the end 
    '''
    @lru_cache(None)
    def dfs(self, i, stateString):
        state = [int(s) for s in stateString.split("_")]
        if i == len(self.Cookies):
            return state[-1]
        else:
            result = float("inf")
            for j in range(len(state)):
                state[j] += self.Cookies[i]
                result = min(result, self.dfs(i + 1, "_".join([str(s) for s in sorted(state)])))
                state[j] -= self.Cookies[i]
            return result
                        
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.Cookies = cookies
        return self.dfs(0, "_".join(["0"] * k))

        
# @lc code=end

