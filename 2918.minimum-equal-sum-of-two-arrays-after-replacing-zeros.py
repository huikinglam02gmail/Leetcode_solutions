#
# @lc app=leetcode id=2918 lang=python3
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#

# @lc code=start
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        left, right, leftS, rightS = 0, 0, 0, 0
        for num1 in nums1:
            if num1 == 0: left += 1
            leftS += num1
        for num2 in nums2:
            if num2 == 0: right += 1
            rightS += num2
        if rightS + right > leftS and left == 0: return -1
        if rightS < leftS + left and right == 0: return -1
        return max(rightS + right, leftS + left)
        
        
# @lc code=end
