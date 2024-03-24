#
# @lc app=leetcode id=3083 lang=python3
#
# [3083] Existence of a Substring in a String and Its Reverse
#

# @lc code=start
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sReverse = s[::-1]
        n = len(s)
        for i in range(n - 1):
            if s[i: i + 2] in sReverse: return True
        return False
# @lc code=end

