#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#

# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        end, n = len(s) - 1, s.count("0")    
        while end >= 0 and int(s[end:], 2) <= k: end -= 1
        return n + s[end + 1:].count("1")
# @lc code=end

