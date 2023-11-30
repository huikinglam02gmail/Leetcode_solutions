#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

# @lc code=start
class Solution:
    '''
    Basic operations procedure:
    1XXXX -> 11000 -> 1000
    We know the answer if n = pow(2, k)
    it is pow(2, k + 1) - 1
    For example, for n = 4, k = 2
    100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000
    Therefore we have f(110) = f(100) - number of operations to go from 100 to 110
    In the second part, the leftmost set bit never changes
    Therefore it is the same as f(10)    
    '''

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0: return 0
        l = n.bit_length()
        return (1 << l) - 1 - self.minimumOneBitOperations(n - (1 << (l - 1)))
# @lc code=end
