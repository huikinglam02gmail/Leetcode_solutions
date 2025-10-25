#
# @lc app=leetcode id=3659 lang=python3
#
# [3659] Partition Array Into K-Distinct Groups
#

# @lc code=start
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // k: return False
        return True
# @lc code=end
