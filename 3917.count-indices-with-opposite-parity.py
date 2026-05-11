#
# @lc app=leetcode id=3917 lang=python3
#
# [3917] Count Indices With Opposite Parity
#

# @lc code=start
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        counts = [0, 0]
        for i in range(len(nums) - 1, -1, -1):
            parity = nums[i] % 2
            result[i] = counts[1 - parity]
            counts[parity] += 1
        return result
# @lc code=end

