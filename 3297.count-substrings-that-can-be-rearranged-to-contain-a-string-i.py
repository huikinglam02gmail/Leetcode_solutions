#
# @lc app=leetcode id=3297 lang=python3
#
# [3297] Count Substrings That Can Be Rearranged to Contain a String I
#

# @lc code=start
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count2 = [0] * 26
        for c in word2:
            count2[ord(c) - ord("a")] += 1
        i = 0
        result = 0
        count1 = [0] * 26
        for j in range(len(word1)):
            count1[ord(word1[j]) - ord("a")] += 1
            while all(count1[k] >= count2[k] for k in range(26)):
                result += len(word1) - j
                count1[ord(word1[i]) - ord("a")] -= 1
                i += 1
        return result
# @lc code=end

