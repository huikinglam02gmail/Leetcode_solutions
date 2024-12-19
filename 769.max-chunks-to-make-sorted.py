#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen, result = 0, 0
        for i, num in enumerate(arr):
            max_seen = max(max_seen, num)
            if max_seen == i: result += 1
        return result
# @lc code=end

