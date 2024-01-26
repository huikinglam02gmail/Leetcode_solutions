#
# @lc app=leetcode id=2614 lang=python3
#
# [2614] Prime In Diagonal
#

# @lc code=start
from typing import List


class Solution:
    '''
    Get all the diagonal elements, sort from high to low
    Sieve of Eratothenes to get all the primes below or equal to max(diagonal)
    report the number if it is inside the prime list
    '''
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diagonals = []
        n = len(nums)
        for i in range(n):
            diagonals.append(nums[i][i])
            diagonals.append(nums[i][n - 1 - i])
        diagonals.sort(reverse=True)
        allPrimes = self.smallestPrimeSieveOfEratosthenes(diagonals[0])
        for d in diagonals:
            if d > 1 and allPrimes[d] == d: return d
        return 0

    '''
    Python program to return smallest prime divisor smaller than or equal to n using Sieve of Eratosthenes 
    '''  
    def smallestPrimeSieveOfEratosthenes(self, n): 
        prime = [i for i in range(n + 1)] 
        p = 2
        while (p * p <= n): 
            if (prime[p] == p):     
                for i in range(p * p, n + 1, p):
                    if prime[i] == i: prime[i] = p
            p += 1
        return prime
# @lc code=end

