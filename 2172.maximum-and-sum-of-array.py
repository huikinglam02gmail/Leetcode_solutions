#
# @lc app=leetcode id=2172 lang=python3
#
# [2172] Maximum AND Sum of Array
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    dp[i][mask] represent we have nums[i:] to add and the current state is represented by "000...000"
    '''
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        maskMapping = [{} for i in range(numSlots)]
        reverseMask = {}
        for mask in range(pow(3, numSlots)):
            maskString = self.convertToTernary(mask).zfill(numSlots)[::-1]
            reverseMask[maskString] = mask
        for mask in range(pow(3, numSlots)):
            maskString = self.convertToTernary(mask).zfill(numSlots)[::-1]
            for j in range(numSlots):
                if int(maskString[j]) < 2: maskMapping[j][mask] = reverseMask[maskString[:j] + str(int(maskString[j]) + 1) + maskString[j + 1:]]
        
        dp = [0 for i in range(pow(3, numSlots))]
        for i in range(len(nums)):
            dpNew = [0 for i in range(pow(3, numSlots))]
            for j in range(numSlots):
                for mask in sorted(maskMapping[j].keys(), reverse=True):
                    dpNew[maskMapping[j][mask]] = max(dpNew[maskMapping[j][mask]], (nums[i] & (j + 1)) + dp[mask])
            dp = dpNew
        return max(dp)

    
    '''
    Function to convert a decimal number to a ternary number
    '''
    def convertToTernary(self, N):
        if N < 3: return str(N)
        x = N % 3
        N //= 3
        return self.convertToTernary(N) + str(x)
# @lc code=end

