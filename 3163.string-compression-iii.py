#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#

# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        word += "A"
        result = ""
        last = "A"
        current = 0
        for i in range(len(word)):
            if word[i] == last and current < 9: current += 1
            elif word[i] == last:
                result += "9" + last
                current = 1
            else:
                result += str(current) + last
                last = word[i]
                current = 1
        return result[2:]


# @lc code=end

