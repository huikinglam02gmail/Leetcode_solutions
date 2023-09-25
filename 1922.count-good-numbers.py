#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start
class Solution:
    '''
    1 <= n <= 10^15
    So we cannot do DP one by one
    but notice this problem is quite simple: even position: 0, 2, 4, 6, 8 => 5 possibilities; odd position: 2, 3, 5, 7
    So, use pow function of python
    '''
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        result = pow(20, n // 2, MOD)
        if n % 2 == 1:
            result *= 5
            result %= MOD
        return result
        
# @lc code=end

