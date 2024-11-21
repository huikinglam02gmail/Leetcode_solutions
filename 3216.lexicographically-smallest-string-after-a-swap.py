#
# @lc app=leetcode id=3216 lang=python3
#
# [3216] Lexicographically Smallest String After a Swap
#

# @lc code=start
class Solution:
    def getSmallestString(self, s: str) -> str:
        result = s
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1] and int(s[i]) % 2 == int(s[i + 1]) % 2: result = min(result, s[:i] + s[i + 1] + s[i] + s[i + 2:])
        return result
# @lc code=end

