#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hash_table = {}
        for i, v in enumerate(arr): hash_table[v] = i
        n, ans = len(arr), 0
        dp = [[2 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for i in range(j):
                diff = arr[j] - arr[i]
                if diff in hash_table and hash_table[diff] < i:
                    dp[i][j] = max(dp[i][j], 1 + dp[hash_table[diff]][i])
                    ans = max(ans, dp[i][j])
        return ans
# @lc code=end

