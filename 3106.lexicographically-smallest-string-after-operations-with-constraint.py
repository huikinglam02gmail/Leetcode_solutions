#
# @lc app=leetcode id=3106 lang=python3
#
# [3106] Lexicographically Smallest String After Operations With Constraint
#

# @lc code=start
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        newString = ""
        for c in s:
            if k > 0:
                steps = min(ord(c) - ord('a'), ord('a') + 26 - ord(c))
                if steps <= k:
                    newString += 'a'
                    k -= steps
                else:
                    newString += chr(ord(c) - k)
                    k = 0
            else: newString += c
        return newString
                    
# @lc code=end

