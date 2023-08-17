#
# @lc app=leetcode id=1850 lang=python3
#
# [1850] Minimum Adjacent Swaps to Reach the Kth Smallest Number
#

# @lc code=start
from typing import List


class Solution:
    '''
    There are two parts of this problem:
    1. Get the kth next permutation
    2. Perform adjacent swaps from num to target
    To perform task 1, use Leetcode 31 k times. O(k * n)
    To perform task 2, use two pointers approach
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1        
        if i >= 0:
            j = n-1
            while j > i and nums[i] >= nums[j]:
                j -= 1                
            nums[i], nums[j] = nums[j], nums[i]
       
        i += 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def getMinSwaps(self, num: str, k: int) -> int:
        target = [int(c) for c in num]
        for i in range(k):
            self.nextPermutation(target)
        original = [int(c) for c in num]
        result = 0
        n = len(original)
        for i in range(n):
            j = i
            while original[j] != target[i]:
                j += 1
            while j > i:
                original[j], original[j - 1] = original[j - 1], original[j]
                j -= 1
                result += 1
        return result
            
# @lc code=end

