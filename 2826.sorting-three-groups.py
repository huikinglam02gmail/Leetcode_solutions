#
# @lc app=leetcode id=2826 lang=python3
#
# [2826] Sorting Three Groups
#

# @lc code=start
from bisect import bisect_right
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(nums) - self.lengthOfLIS(nums)
    
    '''
    Keep a nodecreasing stack of values. When a new number comes, we find it's last smaller element inside the stack (bisectleft). Then we replace the next element with the current number. The final length of the stack is the length of LIS within nums 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for i, num in enumerate(nums):
            if i == 0 or num >= result[-1]: result.append(num)
            else: result[bisect_right(result, num)] = num
        return len(result)
# @lc code=end

