#
# @lc app=leetcode id=2217 lang=python3
#
# [2217] Find Palindrome With Fixed Length
#

# @lc code=start
from typing import List


class Solution:
    '''
    Given intLength, we construct increasing numbers:
    10..0 (ceildiiv(intLength, 2) zeros) to 99..9 (ceildiv(intLenghth, 2) + 1 9s)
    Then for each query q, we add str(q - 1 + base) and its reverse = w
    Concat together to see if it len(int(w)) == intLength
    '''
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = int("1" + "0" * (self.ceildiv(intLength, 2) - 1))
        result = []
        for q in queries:
            result.append(-1)
            frontString = str(q - 1 + base)
            ans = int(frontString + frontString[-1 - intLength % 2::-1])
            if len(str(ans)) == intLength: result[-1] = ans
        return result
    
    '''
    ceil division
    '''
    def ceildiv(self, a, b):
        return -(a // -b)
        
# @lc code=end

