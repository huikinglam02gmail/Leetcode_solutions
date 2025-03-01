#
# @lc app=leetcode id=3456 lang=python3
#
# [3456] Find Special Substring of Length K
#

# @lc code=start
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            if i >= k: counts[ord(s[i - k]) - ord('a')] -= 1
            if (i < k or s[i - k] != s[i - k + 1]) and (i == len(s) - 1 or s[i + 1] != s[i]) and counts[ord(s[i]) - ord('a')] == k: return True
        return False
# @lc code=end

