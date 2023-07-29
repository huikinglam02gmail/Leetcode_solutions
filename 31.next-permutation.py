#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    '''
    A good example is [1,2,4,3]
    Find the first instance in which nums[i - 1] < nums[i], from right to left
    That's the index in which one can exchange between later index -> index 2
    Then we swap the one element before this index with the rightmost element which is larger than this element
    [1, 3, 4, 2]
    finally, we swap everything element between left + 1 and right
    If the sequence is nonincreasing, we swap the whole sequence    
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1        
        if i >= 0:
            j = n-1
            while j > i and nums[i] >= nums[j]:
                j -= 1                
            # exchange
            nums[i], nums[j] = nums[j], nums[i]
       
        i += 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
# @lc code=end

