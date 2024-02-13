#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word) - 1
            while i < j and word[i] == word[j]:
                i += 1
                j -= 1
            if i >= j: return word
        return ""
# @lc code=end

