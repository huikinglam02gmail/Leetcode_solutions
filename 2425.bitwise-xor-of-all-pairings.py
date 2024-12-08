#
# @lc app=leetcode id=2425 lang=python3
#
# [2425] Bitwise XOR of All Pairings
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each num1 in nums1, it is XORed itself len(nums2) times. 
    Then it is XORed with total XOR of nums2 len(nums1) times.
    '''
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums2XOR = 0
        if len(nums1) % 2:
            for num2 in nums2: nums2XOR ^= num2
        nums1XOR = 0
        if len(nums2) % 2:
            for num1 in nums1: nums1XOR ^= num1
        return nums1XOR ^ nums2XOR
        
# @lc code=end

