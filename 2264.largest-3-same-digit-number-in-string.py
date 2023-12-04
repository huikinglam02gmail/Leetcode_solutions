#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    '''
    Find "999" to "000" in num    
    '''
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            search = str(i) * 3
            if search in num: return search
        return ""
# @lc code=end

