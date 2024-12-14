#
# @lc app=leetcode id=2521 lang=python3
#
# [2521] Distinct Prime Factors of Product of Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    2 <= nums[i] <= 1000
    prime factorize all and return total number of keys
    '''
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        total = {}
        for num in nums:
            primes = self.primeFactors(num)
            for k, v in primes.items(): total[k] = total.get(k, 0) + v
        return len(total)

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

