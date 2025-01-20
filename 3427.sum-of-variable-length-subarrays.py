#
# @lc app=leetcode id=3427 lang=python3
#
# [3427] Sum of Variable Length Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums: prefix.append(prefix[-1] + num)
        result = 0
        for i, num in enumerate(nums): result += prefix[i + 1] - prefix[max(0, i - num)]
        return result
        
# @lc code=end

