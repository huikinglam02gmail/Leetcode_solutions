#
# @lc app=leetcode id=3591 lang=python3
#
# [3591] Check if Any Element Has Prime Frequency
#

# @lc code=start
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        allPrimes = set([i for i, isPrime in enumerate(self.SieveOfEratosthenes(len(nums))) if isPrime])
        hashTable = {}
        for num in nums: hashTable[num] = hashTable.get(num, 0) + 1
        for frequency in hashTable.values():
            if frequency in allPrimes: return True
        return False
        
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

