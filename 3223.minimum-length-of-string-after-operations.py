#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        count = [0 for i in range(26)]
        for i in range(len(s)): count[ord(s[i]) - ord('a')] += 1
        result = 0
        for i in range(26):
            if count[i] > 0: result += 1 + (count[i] - 1) % 2
        return result
# @lc code=end

