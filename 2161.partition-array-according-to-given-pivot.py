#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [num for num in nums if num < pivot] + [num for num in nums if num == pivot] + [num for num in nums if num > pivot]
# @lc code=end

