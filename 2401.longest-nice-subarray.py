#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    Number of nice pairs (& = 0) is limited. Just check for every number backwards
    + a number cannot repeat!    
    '''
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result, n = 1, len(nums)
        for i in range(1, n):
            j = i
            current_set = set()
            nice = True
            while j >= 0 and nice:
                for item in current_set: nice &= (item & nums[j] == 0)
                if nice: current_set.add(nums[j])
                j -= 1
            result = max(result, len(current_set))
        return result
# @lc code=end

