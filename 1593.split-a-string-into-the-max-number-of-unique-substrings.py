#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
class Solution:
    '''
    # 1 <= s.length <= 16
    Just backtrack    
    '''
    def dfs(self, i):
        if i == len(self.s):
            self.result = max(self.result, len(self.seen))
        else:
            for j in range(i, len(self.s)):
                if self.s[i:j+1] not in self.seen:
                    self.seen.add(self.s[i:j+1])
                    self.dfs(j+1)
                    self.seen.remove(self.s[i:j+1])

    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0
        self.s = s
        self.seen = set()
        self.dfs(0)
        return self.result
# @lc code=end

