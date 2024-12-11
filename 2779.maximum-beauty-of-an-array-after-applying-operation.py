#
# @lc app=leetcode id=2779 lang=python3
#
# [2779] Maximum Beauty of an Array After Applying Operation
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        
        for num in range(nums[0] - k, nums[-1] + k + 1, 1): result = max(result, bisect.bisect_right(nums, num + k) - bisect.bisect_left(nums, num - k))
        return result
# @lc code=end

