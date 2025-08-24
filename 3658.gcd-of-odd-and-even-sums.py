#
# @lc app=leetcode id=3658 lang=python3
#
# [3658] GCD of Odd and Even Sums
#

# @lc code=start
class Solution:
    '''
    1 + 3 + 5 + ... + (2k - 1) = k^2
    2 + 4 + 6 + ... + (2k) = k * (k + 1)
    '''
    def gcdOfOddEvenSums(self, n: int) -> int:
        return self.gcd(n * n, n * (n + 1))

    '''
    Greatest common divisor between a and b
    Euclidean algorithm
    '''
    def gcd(self, a, b):
        if (a == 0): return b
        else: return self.gcd(b % a, a)
# @lc code=end

