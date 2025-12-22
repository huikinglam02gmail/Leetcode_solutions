#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1
        result = 0
        i = 0
        n = len(nums)
        while i < n and len(occur) < n - i:
            for j in range(min(3, n - i)):
                occur[nums[i]] -= 1
                if occur[nums[i]] == 0: occur.pop(nums[i])
                i += 1
            result += 1
        return result
# @lc code=end

