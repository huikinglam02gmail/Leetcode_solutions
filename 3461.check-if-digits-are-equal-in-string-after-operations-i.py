#
# @lc app=leetcode id=3461 lang=python3
#
# [3461] Check If Digits Are Equal in String After Operations I
#

# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2: return s[0] == s[1]
        newS = ""
        for i in range(len(s) - 1): newS += str((int(s[i]) + int(s[i + 1])) % 10)
        return self.hasSameDigits(newS)

# @lc code=end

