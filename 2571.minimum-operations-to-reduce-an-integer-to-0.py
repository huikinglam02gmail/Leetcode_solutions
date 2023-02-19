#
# @lc app=leetcode id=2571 lang=python3
#
# [2571] Minimum Operations to Reduce an Integer to 0
#

# @lc code=start
class Solution:
    '''
    first convert n into its binary form
    For example: 39 as 100111
    We notice this: 
    1. In the simple scenarios of a bit was originally 0 / 1, adding / subtracting power of 2 means flipping 0 to 1 / 1 to 0
        The first scenario means we have to flip the bit back to 0 in further operations, which is undesirable
        The second scenario would count against routine operations in the minimum operation move
    2. In the second scenario, the bit was originally 1 / 0. Again, flips in the second scenario leads to extra steps to revert back, and therefore is ignored.
        However in the first scenario, if we add 1 to the current bit, we would benefit if we have 2 or more consecutive 1s left of it. 
    '''
    def minOperations(self, n: int) -> int:
        l =  n.bit_length()
        result = 0
        for i in range(l + 1):
            if (n & (1 << i) != 0):
                if ((n + (1 << i)).bit_count() < n.bit_count()):
                    n += 1 << i
                result += 1
        return result
        
# @lc code=end
