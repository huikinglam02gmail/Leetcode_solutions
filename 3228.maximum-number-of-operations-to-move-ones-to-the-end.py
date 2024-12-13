#
# @lc app=leetcode id=3228 lang=python3
#
# [3228] Maximum Number of Operations to Move Ones to the End
#

# @lc code=start
class Solution:
    '''
    Consecutive '0's do not matter. For each '0', it will be passed by # of '1's before it
    '''
    def maxOperations(self, s: str) -> int:
        count = 0
        result = 0
        i = 0
        while i < len(s):
            if s[i] == '0':
                while i + 1 < len(s) and s[i + 1] == '0': i += 1
                result += count
            else:
                count += 1
            i += 1
        return result

# @lc code=end

