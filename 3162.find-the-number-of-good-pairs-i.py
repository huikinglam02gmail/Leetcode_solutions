#
# @lc app=leetcode id=3162 lang=python3
#
# [3162] Find the Number of Good Pairs I
#

# @lc code=start
from typing import List


class Solution:
    '''
    multiply all nums2 by k first
    sort both
    for each num1, for num2 <= num1, ask if num1 % num2 == 0
    '''
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        for i in range(len(nums2)): nums2[i] *= k
        nums2.sort()
        result = 0
        for num1 in nums1:
            i = 0
            while i < len(nums2) and nums2[i] <= num1:
                if num1 % nums2[i] == 0: result += 1
                i += 1
        return result
# @lc code=end
