#
# @lc app=leetcode id=1638 lang=python3
#
# [1638] Count Substrings That Differ by One Character
#

# @lc code=start
class Solution:
    # For each s[i] != t[j], 
    # we ask how many equals is before and after it
    # we take the product and add to the result
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        before = [[0 for j in range(n)] for i in range(m)]
        after = [[0 for j in range(n)] for i in range(m)]    
        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    before[i][j] = before[i - 1][j - 1] + 1
                else:
                    before[i][j] = 0
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if s[i + 1] == t[j + 1]:
                    after[i][j] = after[i + 1][j + 1] + 1
                else:
                    after[i][j] = 0 
        result = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    result += (before[i][j] + 1) * (after[i][j] + 1)
        return result                   

        
# @lc code=end