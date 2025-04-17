#
# @lc app=leetcode id=3517 lang=python3
#
# [3517] Smallest Palindromic Rearrangement I
#

# @lc code=start
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        occur = [0] * 26
        for c in s: occur[ord(c) - ord('a')] += 1
        left = ""
        for i in range(26): left += (occur[i] // 2) * chr(ord('a') + i)
        middle = ""
        for i in range(26):
            if occur[i] % 2 == 1: middle = chr(ord('a') + i)
        return left + middle + left[::-1]
            
# @lc code=end

