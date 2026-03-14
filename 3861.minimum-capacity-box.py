#
# @lc app=leetcode id=3861 lang=python3
#
# [3861] Minimum Capacity Box
#

# @lc code=start
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        result = -1
        current = float('inf')
        for i, cap in enumerate(capacity):
            if itemSize <= cap < current:
                result = i
                current = cap
        return result
# @lc code=end

