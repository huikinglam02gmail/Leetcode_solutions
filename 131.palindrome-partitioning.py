#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,[],res)
        return res
        
    def isPalindrome(self, s):
        return s == s[::-1]

    def dfs(self, s, path, res):
        if not s:
            res.append(path)

        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
        
# @lc code=end

