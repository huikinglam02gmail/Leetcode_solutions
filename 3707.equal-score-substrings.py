#
# @lc app=leetcode id=3707 lang=python3
#
# [3707] Equal Score Substrings
#

# @lc code=start
class Solution:
    def scoreBalance(self, s: str) -> bool:
        seen = set()
        prefix = 0
        for c in s:
            prefix += ord(c) - ord('a') + 1
            seen.add(prefix)
        return prefix % 2 == 0 and (prefix // 2) in seen
# @lc code=end

