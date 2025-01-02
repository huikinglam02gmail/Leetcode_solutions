#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        minSoFar = float("inf")
        result = [- float("inf"), -float("inf")]
        lastPrime = - float("inf")
        for i in range(left, right + 1, 1):
            if self.isPrime(i):
                if i - lastPrime < minSoFar: 
                    result = [lastPrime, i]
                    minSoFar = i - lastPrime
                lastPrime = i
        return [-1, -1] if minSoFar == float("inf") else result

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
        
# @lc code=end

