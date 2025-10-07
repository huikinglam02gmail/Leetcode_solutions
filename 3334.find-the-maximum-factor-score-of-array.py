#
# @lc app=leetcode id=3334 lang=python3
#
# [3334] Find the Maximum Factor Score of Array
#

# @lc code=start
from typing import List
import math


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefixGCD = [0] * (n + 1)
        suffixGCD = [0] * (n + 1)
        prefixLCM = [1] * (n + 1)
        suffixLCM = [1] * (n + 1)
        for i in range(n):
            prefixGCD[i + 1] = self.gcd(prefixGCD[i], nums[i])
            prefixLCM[i + 1] = prefixLCM[i] * nums[i] // self.gcd(prefixLCM[i], nums[i])
        for i in range(n - 1, -1, -1):
            suffixGCD[i] = self.gcd(suffixGCD[i + 1], nums[i])
            suffixLCM[i] = suffixLCM[i + 1] * nums[i] // self.gcd(suffixLCM[i + 1], nums[i])
        result = prefixGCD[n] * prefixLCM[n]
        for i in range(1, n + 1):
            result = max(result, math.gcd(prefixGCD[i - 1], suffixGCD[i]) * math.lcm(prefixLCM[i - 1], suffixLCM[i]))
        return result
    
    '''
    Greatest common divisor between a and b
    Euclidean algorithm
    '''
    def gcd(self, a, b):
        if (a == 0): return b
        else: return self.gcd(b % a, a)

# @lc code=end

