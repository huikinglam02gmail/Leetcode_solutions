#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, result = 0, 0, []
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            result.append(word1[i])
            i += 1
        while j < len(word2):
            result.append(word2[j])
            j += 1
        return "".join(result)

# @lc code=end

