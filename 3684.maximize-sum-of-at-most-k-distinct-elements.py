#
# @lc app=leetcode id=3684 lang=python3
#
# [3684] Maximize Sum of At Most K Distinct Elements
#

# @lc code=start
from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), reverse=True)[:min(k, len(set(nums)))]
# @lc code=end

