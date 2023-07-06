#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    binary search approach:
    since we want the subarray sum, why not first calculate prefix sum?
    Since all numbers are positive, one can do binary search for all indices to look for the right index    
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
        result = len(nums) + 1
        for i in range(len(prefix)-1):
            index = bisect.bisect_left(prefix, prefix[i] + target)
            if index < len(prefix):
                result = min(result, index - i)
        return result if result < len(nums) + 1 else 0
# @lc code=end
