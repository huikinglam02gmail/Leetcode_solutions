#
# @lc app=leetcode id=1735 lang=python3
#
# [1735] Count Ways to Make Array With Product
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    For all k given, we want to first prime factorize it first
    To k = p1^i1 * p2^i2 * ... * pn^in
    Note 1 is not a prime, but essentially it is px^0
    For example, if n = 3 and k = 12 = 2^2 * 3^1
    First think about putting in the 2s, let's represent the n = 3 positions as separated by "|" and the 2 2s and 2 "*"
    Then there are 6 possibilities:
    [4,1,1]: "**||"; [1,4,1]:"|**|"; [1,1,4]="||**"; [2,2,1]="*|*|"; [2,1,2]="*||*"; [1,2,2]="|*|*"
    So we see given we have n positions and r factors of p in prime factorization of k, contribution by p is given by (n + r - 1) C (n - 1)
    Going through each prime and multiply the contribution together will give the answer
    '''

    def primeFactors(self, n):
        primes = {}
        while n % 2 == 0:
            primes[2] = primes.get(2, 0) + 1
            n //= 2

        i = 3
        while i*i <= n:
            while n % i == 0:
                primes[i] = primes.get(i, 0) + 1
                n //= i
            i += 2

        if n > 1:
            primes[n] = primes.get(n, 0) + 1
        return primes

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        results = []
        for n, k in queries:
            kPrimeFactors = self.primeFactors(k)
            result = 1
            for p, v in kPrimeFactors.items():
                result *= (math.comb(n + v - 1, n - 1) % MOD)
                result %= MOD
            results.append(result)
        return results
        
# @lc code=end

