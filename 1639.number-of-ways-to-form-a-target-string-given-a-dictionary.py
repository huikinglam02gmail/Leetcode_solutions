#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#

# @lc code=start
from typing import List


class Solution:
    # We can form target like this:
    # for each index i in word, we count how many times each character occur
    # Then we try to form target from back to front
    # For example, if target is "abc", we first look at how many "ab"s we have previously formed
    # i.e. dp[i][j] = number of ways to form target[n - j:] after we considered index i
    # We are looking for dp[m - 1][n]
    def numWays(self, words: List[str], target: str) -> int:
        m, n, MOD = len(words[0]), len(target), pow(10, 9) + 7
        dp = [1] + [0]*n
        for i in range(m):
            seen = [0]*26
            for word in words:
                seen[ord(word[i]) - ord('a')] += 1
            for j in range(n - 1, -1, -1):
                dp[j + 1] += dp[j] * seen[ord(target[j]) - ord('a')]
                dp[j + 1] %= MOD
        return dp[-1]
# @lc code=end

