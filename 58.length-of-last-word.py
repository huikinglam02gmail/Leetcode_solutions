#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    '''
    Add " " in front and after s
    Pick up where s[i] == " " and s[i + 1] != " ", and s[j] != " " and s[j + 1] == " "
    '''
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s + " "
        l, r = 0, 0
        for i in range(len(s) - 1):
            if s[i] == " " and s[i + 1] != " ": l = i
            if s[i] != " " and s[i + 1] == " ": r = i
        return r - l
# @lc code=end

