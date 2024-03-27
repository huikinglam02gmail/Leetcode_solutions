#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        seen = [0] * 26
        result = 0
        for right, c in enumerate(s):
            while seen[ord(c) - ord('a')] == 2:
                seen[ord(s[left]) - ord('a')] -= 1
                left += 1
            seen[ord(c) - ord('a')] += 1
            result = max(result, right - left + 1)
        return result
# @lc code=end

