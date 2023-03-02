#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    To avoid nuisances of array indices, we instead use odd and even prefix dictionaries to record prefix sum
    '''
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefixOdd = {}
        prefixEven = {}
        prefixOdd[-1] = 0
        prefixEven[-2] = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                prefixEven[i] = prefixEven[i - 2] + num
            else:
                prefixOdd[i] = prefixOdd[i - 2] + num
        
        result = 0
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                leftEvenSum = prefixEven[i - 2] - prefixEven[-2]
                leftOddSum = prefixOdd[i - 1] - prefixOdd[-1]
                if n % 2 == 0:
                    rightEvenSum = prefixEven[n - 2] - prefixEven[i]
                    rightOddSum = prefixOdd[n - 1] - prefixOdd[i - 1]
                else:
                    rightEvenSum = prefixEven[n - 1] - prefixEven[i]
                    rightOddSum = prefixOdd[n - 2] - prefixOdd[i - 1]
            else:
                leftEvenSum = prefixEven[i - 1] - prefixEven[-2]
                leftOddSum = prefixOdd[i - 2] - prefixOdd[-1]
                if n % 2 == 0:
                    rightEvenSum = prefixEven[n - 2] - prefixEven[i - 1]
                    rightOddSum = prefixOdd[n - 1] - prefixOdd[i]
                else:
                    rightEvenSum = prefixEven[n - 1] - prefixEven[i - 1]
                    rightOddSum = prefixOdd[n - 2] - prefixOdd[i]      
            if leftEvenSum + rightOddSum == leftOddSum + rightEvenSum:
                result += 1
        return result                          
                
        
# @lc code=end

