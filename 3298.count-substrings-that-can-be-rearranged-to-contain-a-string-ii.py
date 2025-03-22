#
# @lc app=leetcode id=3298 lang=python3
#
# [3298] Count Substrings That Can Be Rearranged to Contain a String II
#

# @lc code=start
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count = [0] * 26
        for c in word2: count[ord(c) - ord('a')] += 1
        l = 0
        result = 0
        fit = 0
        for i in range(26):
            if count[i] == 0: fit += 1
        for r in range(len(word1)):
            count[ord(word1[r]) - ord('a')] -= 1
            if count[ord(word1[r]) - ord('a')] == 0: fit += 1 
            while fit == 26:
                count[ord(word1[l]) - ord('a')] += 1
                if count[ord(word1[l]) - ord('a')] == 1: fit -= 1
                l += 1
            result += l
        return result
# @lc code=end

