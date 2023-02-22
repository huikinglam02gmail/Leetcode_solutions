#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    log n: must use binary search, cannot use the bit manipulation trick
    Two simple examples: 
    1. 5 distinct elements: mid % 2 = 0
    [1,1,2,3,3,4,4,8,8]
    [1,1,2,2,3,3,4,8,8]
    2. 4 distinct elements: mid % 2 != 0
    [3,3,7,7,10,11,11]
    [3,3,7,10,10,11,11]       
    length of string must be odd
    mid element (len(nums)) // 2 must be the middle element
    the element we want is the only element nums[mid-1] < nums[mid] < nums[mid+1]     
    '''
   
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n // 2 
        if mid > 0 and mid < n - 1 and nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if mid % 2 == 0:
            if nums[mid + 1] != nums[mid]:
                return self.singleNonDuplicate(nums[:mid - 1])
            else:
                return self.singleNonDuplicate(nums[mid + 2:])
        else:
            if nums[mid + 1] != nums[mid]:
                return self.singleNonDuplicate(nums[mid + 1:])
            else:
                return self.singleNonDuplicate(nums[:mid])
# @lc code=end

