#
# @lc app=leetcode id=1808 lang=python3
#
# [1808] Maximize Number of Nice Divisors
#

# @lc code=start
class Solution:
    '''
    This problem does not require prime factorization. Suppose num = (p1 ^ a1) * (p2 ^ a2) * ... * (pi ^ ai) * ... * (pn ^ an), and a1 + a2 + ... + an = primeFactors. The number of nice divisors is therefore a1 * a2 * a3 * .... * an. This is exactly the same problem statement as Leetcode 343: Integer Break. So just copy the solution from there. However there is minor difference: In 343, n is required to break into more than 1 part, whereas in here there are no such requirement. So just update the side cases. Also, this time primeFactors can be very large, so we should not do the minus 3 one by one. Instead we should use the pow with modulo function, provided in Python
    '''
        
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = pow(10, 9) + 7
        if primeFactors == 1:
            return 1
        elif primeFactors  == 2:
            return 2
        else:
            a, b = divmod(primeFactors, 3)
            if b == 0:
                return pow(3, a, MOD)
            elif b == 1:
                return (pow(3, a - 1, MOD) * 4) % MOD
            elif b == 2:
                return (pow(3, a, MOD) * 2) % MOD
        
# @lc code=end

