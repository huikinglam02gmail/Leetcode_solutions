#
# @lc app=leetcode id=3556 lang=python3
#
# [3556] Sum of Largest Prime Substrings
#

# @lc code=start
import math


class Solution:
    '''
    Function that returns True if n is prime else returns False    
    ''' 
    def isPrime(self, n):        
        if(n <= 1): return False
        if(n <= 3): return True
        
        if(n % 2 == 0 or n % 3 == 0): return False
        
        for i in range(5,int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0): return False       
        return True
    
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isPrime(int(s[i:j])): primes.add(int(s[i:j]))
        
        primes = sorted(primes, reverse=True)
        result = 0
        for i in range(min(3, len(primes))): result += primes[i]
        return result
# @lc code=end

