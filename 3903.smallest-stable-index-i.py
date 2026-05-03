#
# @lc app=leetcode id=3903 lang=python3
#
# [3903] Smallest Stable Index I
#

# @lc code=start
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        stability = [0] * len(nums)
        current = 0
        for i in range(len(nums)):
            current = max(current, nums[i])
            stability[i] = current
        current = float("inf")
        for i in range(len(nums) - 1, -1, -1):
            current = min(current, nums[i])
            stability[i] -= current
        for i in range(len(nums)):
            if stability[i] <= k: return i
        return -1

# @lc code=end

