#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Keep a hashTable to keep occurrence of each number
    Keep an array of occurrence: arr[i] = items which occurs i + 1 times. Use a sortedList to get the largest elements easily.
    We first scan nums from nums[0] to nums[k - 1]. 
    The top x elements can be added by scanning from high to low occurence, each num will contribute occur * num to the sum.
    To easily find what contributed to the sum, we record what and how many 
    Then we shift right, 1 nums[0] got removed. And 1 nums[k] got added. 
    '''
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
# @lc code=end

