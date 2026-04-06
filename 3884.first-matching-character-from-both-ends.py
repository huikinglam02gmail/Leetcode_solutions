#
# @lc app=leetcode id=3884 lang=python3
#
# [3884] First Matching Character From Both Ends
#

# @lc code=start
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                return i
            i += 1
            j -= 1
        return -1
# @lc code=end

