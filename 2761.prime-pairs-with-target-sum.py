#
# @lc app=leetcode id=2761 lang=python3
#
# [2761] Prime Pairs With Target Sum
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes
    '''
    def SieveOfEratosthenes(self, n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return prime
    
    def findPrimePairs(self, n: int) -> List[List[int]]:
        result = []
        allPrimes = self.SieveOfEratosthenes(n)
        for i in range(2, n // 2 + 1):
            if allPrimes[i] and allPrimes[n - i]: result.append([i, n - i])
        return result
# @lc code=end

