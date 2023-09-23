#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a variation of the LIS problem. How to convert?
    The definition of predecessor:
    wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB
    LIS condition: nums[i] < nums[j]
    Longest string chain condition: s[i] is subsequence of s[j]
    important: len(s[i]) == len(s[j]) - 1 Otherwise no need consider
    To find the latter, we reuse function written in Leetcode 392 Is Subsequence
    and Leetcode 673 Number of Longest Increasing Subsequence    
    '''

    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)
    
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        n = len(words)
        dp = [1 for i in range(n)]
        for j in range(n - 2, -1, -1):
            for k in range(j + 1, n, 1):
                if len(words[j]) == len(words[k]) - 1 and self.isSubsequence(words[j],words[k]):
                    dp[j] = max(dp[j], dp[k] + 1)
        return max(dp)
# @lc code=end

