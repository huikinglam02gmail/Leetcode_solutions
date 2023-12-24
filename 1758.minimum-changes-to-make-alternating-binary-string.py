#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        S = [0, 0]
        for i in range(len(s)): S[1 - i % 2 - pow(-1, i % 2) * (ord(s[i]) - ord('0'))] += 1
        return min(S)
# @lc code=end

