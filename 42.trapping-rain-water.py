#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    '''
    Classic problem to be solved by dynamic programming
    Water trapped at i = min(highest seen on its left, highest seen on its right) - height[i]
    '''
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, n): left_max[i] = max(height[i], left_max[i - 1])
        for i in range(n - 2, -1, -1): right_max[i] = max(height[i], right_max[i + 1])
        for i in range(n): result += min(left_max[i], right_max[i]) - height[i]
        return result
# @lc code=end

