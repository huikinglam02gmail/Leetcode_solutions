#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
from typing import List


class Solution:
    '''
    Any number AND with a smaller number will result in a number smaller than itself
    So the answer in the number length of consecutive max
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        maxSoFar = 0
        maxSoFarLength = 0
        last = 0
        current = 0
        for num in nums:
            if num == last: 
                current += 1
            else:
                if last > maxSoFar: 
                    maxSoFar = last
                    maxSoFarLength = current
                elif last == maxSoFar:
                    maxSoFarLength = max(maxSoFarLength, current)
                last = num
                current = 1
        return maxSoFarLength
        
# @lc code=end
