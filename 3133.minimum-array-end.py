#
# @lc app=leetcode id=3133 lang=python3
#
# [3133] Minimum Array End
#

# @lc code=start
class Solution:
    '''
    The first element must be x. In all following elements, we are filling in all 0 bits of x with either 0 or 1
    '''
    def minEnd(self, n: int, x: int) -> int:
        bx, bn = 1, 1
        while bn < n:
            if (bx & x) == 0:
                if bn & (n - 1): x += bx 
                bn <<= 1
            bx <<= 1
        return x
# @lc code=end

