#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
class Solution:
    '''
    Combinatorics problem
    Look at Example 2 to get some hints
    Check out where can P1 be: if n = 2, P1 can be at position 0, 1, 2, but not 3, i.e. 2 * n - 1 possibilities. 
    And there are two Ps, so the permutations are n * (2 * n - 1)
    So this problem is about where can we place the Ps    
    '''

    def countOrders(self, n: int) -> int:
        result, MOD = 1, pow(10,9) + 7
        for i in range(2, n + 1):
            result *= i * (2 * i - 1)
            result %= MOD
        return result
        
# @lc code=end

