#
# @lc app=leetcode id=3803 lang=python3
#
# [3803] Count Residue Prefixes
#

# @lc code=start
class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = {}
        result = 0
        for i, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1
            if len(seen) == (i + 1) % 3:
                result += 1
        return result
# @lc code=end

