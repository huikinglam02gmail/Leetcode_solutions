#
# @lc app=leetcode id=3702 lang=python3
#
# [3702] Longest Subsequence With Non-Zero Bitwise XOR
#

# @lc code=start
from typing import List


class Solution:
    '''
    3 possible answers:
    1. If total XOR != 0, return len(nums)
    2. If there exists an element that is not 0, return len(nums) - 1
    3. Otherwise, return 0
    '''
    def longestSubsequence(self, nums: List[int]) -> int:
        nonZero_exists = False
        total_xor = 0
        for num in nums:
            total_xor ^= num
            if num != 0: nonZero_exists = True
        if total_xor != 0: return len(nums)
        elif nonZero_exists: return len(nums) - 1
        else: return 0
# @lc code=end

