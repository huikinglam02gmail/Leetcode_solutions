#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just do as described
    '''
    def evenOddBit(self, n: int) -> List[int]:
        nString = bin(n)[2:][::-1]
        result = [0, 0]
        for i, c in enumerate(nString):
            if c == "1": result[i % 2] += 1
        return result
        
# @lc code=end

