#
# @lc app=leetcode id=3210 lang=python3
#
# [3210] Find the Encrypted String
#

# @lc code=start
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        shift = k % len(s)
        return s[shift:] + s[:shift]
# @lc code=end

