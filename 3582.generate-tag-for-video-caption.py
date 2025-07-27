#
# @lc app=leetcode id=3582 lang=python3
#
# [3582] Generate Tag for Video Caption
#

# @lc code=start
class Solution:
    def generateTag(self, caption: str) -> str:
        captionSplit = caption.lstrip(" ").rstrip(" ").split(" ")
        result = "#"
        for i, s in enumerate(captionSplit):
            for j in range(len(s)):
                if s[j].isalpha():
                    if i > 0 and j == 0:
                        result += s[j].upper()
                    else:
                        result += s[j].lower()
                    if len(result) >= 100: return result
        return result

# @lc code=end

