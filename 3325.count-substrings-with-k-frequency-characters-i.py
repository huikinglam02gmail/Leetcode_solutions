#
# @lc app=leetcode id=3325 lang=python3
#
# [3325] Count Substrings With K-Frequency Characters I
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        result = 0
        counts = [0] * 26
        n = len(s)
        left = 0
        for i, c in enumerate(s):
            counts[ord(c) - ord('a')] += 1
            while counts[ord(c) - ord('a')] >= k:
                result += n - i
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1
        return result
# @lc code=end

