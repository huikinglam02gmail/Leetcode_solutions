#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List
class Solution:
    '''
    Keep a monotonic increasing stack of values. When a new number comes, we find it's last smaller element inside the stack (bisectleft). Then we replace the next element with the current number. The final length of the stack is the length of LIS within nums 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        for i, num in enumerate(nums):
            if i == 0 or num > result[-1]: result.append(num)
            else: result[bisect.bisect_left(result, num)] = num
        return len(result)
# @lc code=end

