#
# @lc app=leetcode id=3233 lang=python3
#
# [3233] Find the Count of Numbers Which Are Not Special
#

# @lc code=start
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        S1 = 0
        S2 = 0
        n = 0
        count = 0
        while n * n <= r: n += 1
        allPrimes = self.SieveOfEratosthenes(n)
        for i in range(n + 1):
            if allPrimes[i]:
                count += 1
                if i * i < l: S1 = count
                if i * i <= r: S2 = count
        return r - l + 1 - S2 + S1
    
    '''
    Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes
    '''
    def SieveOfEratosthenes(self, n):
        prime = [True for i in range(n + 1)]
        prime[0] = prime[1] = False
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return prime
# @lc code=end

