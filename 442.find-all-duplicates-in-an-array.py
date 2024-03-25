#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use array index as hash_key
    when you see a number i in an array, just add the array length n to the ith element
    the original number can be recovered by getting num % n
    duplicates would be added 2 times and can be easily identified by the corresponding index    
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums: nums[num % n - 1] += n
        result = []
        for i in range(n):
            if nums[i] > 2 * n: result.append(i+1)
        return result
# @lc code=end

