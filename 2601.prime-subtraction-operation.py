#
# @lc app=leetcode id=2601 lang=python3
#
# [2601] Prime Subtraction Operation
#

# @lc code=start
import bisect
import math
from typing import List


class Solution:
    '''
    1 <= nums[i] <= 1000
    So first all primes 1 <= x <= 1000
    Then for each num[i], look for p such that p < nums[i] and num[i - 1] < num[i] - p, i.e p < num[i] - num[i - 1]
    '''
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        for i in range(2, 1001):
            if self.isPrime(i): primes.append(i)
        
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                ind = bisect.bisect_left(primes, nums[i] - nums[i - 1])
                if ind > 0: nums[i] -= primes[ind - 1]
            elif nums[i] <= nums[i - 1]: return False
        return True
        
    '''
    Function that returns True if n is prime else returns False    
    ''' 
    def isPrime(self, n):        
        if(n <= 1):
            return False
        if(n <= 3):
            return True
        
        if(n % 2 == 0 or n % 3 == 0):
            return False
        
        for i in range(5,int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0):
                return False
        
        return True

# @lc code=end

