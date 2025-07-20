#
# @lc app=leetcode id=3618 lang=python3
#
# [3618] Split Array by Prime Indices
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        result = [0, 0]
        allPrimes = self.SieveOfEratosthenes(len(nums))
        for i in range(len(nums)):
            if allPrimes[i]:
                result[0] += nums[i]
            else:
                result[1] += nums[i]
        return abs(result[0] - result[1])
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

