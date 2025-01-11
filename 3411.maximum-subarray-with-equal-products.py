#
# @lc app=leetcode id=3411 lang=python3
#
# [3411] Maximum Subarray With Equal Products
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= nums[i] <= 10
    The answer is the longest coprime array
    '''
    def maxLength(self, nums: List[int]) -> int:
        l = 0
        current = set()
        result = 2
        for r in range(len(nums)):
            primes = self.primeFactors(nums[r])
            for prime in primes:
                while prime in current:
                    lPrimes = self.primeFactors(nums[l])
                    for lPrime in lPrimes: current.remove(lPrime)
                    l += 1
                current.add(prime)
            result = max(result, r - l + 1)
        return result
                
    
    '''
    A function to store the prime factor as key and power as value in a dictionay 
    '''
    def primeFactors(self, n):
        primes = {}
        while n % 2 == 0:
            primes[2] = primes.get(2, 0) + 1
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                primes[i] = primes.get(i, 0) + 1
                n //= i
            i += 2
        if n > 1:
            primes[n] = primes.get(n, 0) + 1
        return primes
            

# @lc code=end
