#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1, 1):
            if len(s) % i == 0 and s == s[:i] * (len(s) // i):
                return True
        return False

# @lc code=end

