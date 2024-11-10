#
# @lc app=leetcode id=3097 lang=python3
#
# [3097] Shortest Subarray With OR at Least K II
#

# @lc code=start
from typing import List


class Solution:
    def getOrFromCounts(self):
        result = 0
        for i in range(32):
            if self.counts[i] > 0: result += (1 << i)
        return result
    
    def canRemoveNum(self, num, k):
        for i in range(32):
            if num & (1 << i): self.counts[i] -= 1
        candidate = self.getOrFromCounts()
        if candidate < k:
            for i in range(32):
                if num & (1 << i): self.counts[i] += 1
            return False
        else:
            self.current = candidate
            return True          
    
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = len(nums) + 1
        l = 0
        self.counts = [0] * 32
        self.current = 0
        for r in range(len(nums)):
            self.current |= nums[r]
            for i in range(32):
                if nums[r] & (1 << i): self.counts[i] += 1
            while l < r and self.canRemoveNum(nums[l], k):
                l += 1
            if self.current >= k: result = min(result, r - l + 1)
        return result if result <= len(nums) else -1


# @lc code=end

