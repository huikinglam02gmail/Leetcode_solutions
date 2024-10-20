#
# @lc app=leetcode id=2957 lang=python3
#
# [2957] Remove Adjacent Almost-Equal Characters
#

# @lc code=start
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        result, i = 0, 1
        while i < len(word):
            if abs(ord(word[i]) - ord(word[i - 1])) < 2: 
                result += 1
                i += 2
            else: i += 1
        return result
# @lc code=end

