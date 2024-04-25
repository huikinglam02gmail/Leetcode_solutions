#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            curr = 0
            for i in range(index - k, index + k + 1, 1):
                if 0 <= i < 26: curr = max(curr, dp[i] + 1)
            dp[index] = curr
        return max(dp)
# @lc code=end

