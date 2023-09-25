#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = [0] * 26
        tCount = [0] * 26
        for c in s:
            sCount[ord(c) - ord('a')] += 1
        for c in t:
            tCount[ord(c) - ord('a')] += 1
        for i in range(26):
            if sCount[i] != tCount[i]:
                return chr(i + ord('a'))
        return ""     

# @lc code=end

