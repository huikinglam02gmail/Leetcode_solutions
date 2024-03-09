#
# @lc app=leetcode id=3019 lang=python3
#
# [3019] Number of Changing Keys
#

# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        result, n = 0, len(s)
        for i in range(n - 1):
            if s[i + 1].lower() != s[i].lower(): result += 1
        return result
# @lc code=end

