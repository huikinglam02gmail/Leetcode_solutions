#
# @lc app=leetcode id=3583 lang=python3
#
# [3583] Count Special Triplets
#

from typing import List

# @lc code=start
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = {}
        leftCount = [0] * len(nums)
        right = {}
        rightCount = [0] * len(nums)
        for i in range(len(nums)):
            leftCount[i] += left.get(2 * nums[i], 0)
            left[nums[i]] = left.get(nums[i], 0) + 1
        for i in range(len(nums) - 1, -1, -1):
            rightCount[i] += right.get(2 * nums[i], 0)
            right[nums[i]] = right.get(nums[i], 0) + 1
        result = 0
        MOD = pow(10, 9) + 7
        for i in range(len(nums)):
            result += leftCount[i] * rightCount[i]
            result %= MOD
        return result
# @lc code=end

