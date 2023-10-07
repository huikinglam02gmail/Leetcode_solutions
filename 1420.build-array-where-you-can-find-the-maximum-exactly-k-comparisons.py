#
# @lc app=leetcode id=1420 lang=python3
#
# [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    This is a DP problem
    Let dp(i, j, l) = the number of ways to build an array with length i, max(arr) = j, and the search cost is l
    Then we try to break down into subproblems
    1. The number j in arr[:i] occured before i. 
    A good example is given in Example 1, in which in [3,1], [3,2], [3,3] the number 3 occurs before the position 1
    Therefore we can put any x between 1 and j at position i
    and have this recurrence relation: dp(i, j, l) += j*dp(i-1,j,l)
    2. The number j in arr[:i] only occurred at i. 
    Then the arr[:i-1] could have maximum anywhere between 1 and j-1
    To achieve search cost of l at position i, the corresponding cost before must be l-1
    Therefore dp(i, j, l) += dp(i - 1, x, l - 1), loop x from 1 to j-1
    Base cases: dp(1, j, 1) = 1, any other l will give 0
    We want sum of dp(n,x,k), with x looping from 1 to m    
    '''    
    @lru_cache(None)
    def dp(self, i, j, l):
        result = 0
        if i == 1 and l == 1:
            result += 1
        elif i > 1:
            result += j * self.dp(i - 1, j, l)
            result %= self.MOD
            if l > 1:
                for x in range(1,j):
                    result += self.dp(i - 1, x, l - 1)
                    result %= self.MOD
        return result
     
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.MOD = pow(10,9) + 7
        final = 0
        for i in range(1,m + 1):
            final += self.dp(n, i, k)
            final %= self.MOD
        return final
# @lc code=end

