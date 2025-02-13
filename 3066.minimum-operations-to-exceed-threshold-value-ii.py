#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2 * min(x, y) + max(x, y))
            count += 1
        return count

# @lc code=end

