#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        count = {}
        current_sum = 0
        max_sum = 0
        for i in range(k):
            count[nums[i]] = count.get(nums[i], 0) + 1
            current_sum += nums[i]
            if len(count) >= m: max_sum = max(max_sum, current_sum)        
        for i in range(k, n):
            count[nums[i]] = count.get(nums[i], 0) + 1
            current_sum += nums[i]
            count[nums[i - k]] -= 1
            current_sum -= nums[i - k]
            if count[nums[i - k]] == 0: count.pop(nums[i - k])
            if len(count) >= m: max_sum = max(max_sum, current_sum)
        return max_sum
# @lc code=end

