#
# @lc app=leetcode id=3115 lang=python3
#
# [3115] Maximum Prime Difference
#

# @lc code=start
import math
from typing import List


class Solution:  
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primeIndices = []
        for i, num in enumerate(nums):
            if self.isPrime(num): primeIndices.append(i)
        return primeIndices[-1] - primeIndices[0]

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

