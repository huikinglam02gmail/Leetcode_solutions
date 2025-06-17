#
# @lc app=leetcode id=3405 lang=python3
#
# [3405] Count the Number of Arrays with K Matching Adjacent Elements
#

# @lc code=start
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1000000007
        result = m
        result *= pow(m - 1, n - 1 - k, MOD)
        result *= self.combinations_mod(n - 1, k, MOD)
        result %= MOD
        return result
    
    """
    Computes C(n, k) modulo p.

    Args:
    n: The total number of items.
    k: The number of items to choose.
    p: The modulus (usually a prime number).

    Returns:
    The value of C(n, k) modulo p.
    """
    def combinations_mod(self, n, k, p):
        if k < 0 or k > n: return 0
        if k == 0 or k == n: return 1
        if k > n // 2: k = n - k

        result = 1
        for i in range(k):
            result *= (n - i)
            result %= p
            result *= pow(i + 1, p - 2, p)
            result %= p
        return result
# @lc code=end

