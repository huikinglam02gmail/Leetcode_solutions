#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    '''
    Dutch national flag problem
    Keep three pointers to move things in place and do it in only 1 pass
    Keep looking at the middle pointer
    if it is 1, move forward by 1
    if it is 2, exchange with two
    if it is 0, exchange with zero    
    '''
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, len(nums)-1
        while one <= two:
            if nums[one] == 1:
                one += 1
            elif nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1
                # @lc code=end

