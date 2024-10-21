#
# @lc app=leetcode id=3285 lang=python3
#
# [3285] Find Indices of Stable Mountains
#

# @lc code=start
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        result = []
        for i in range(1, len(height), 1):
            if height[i - 1] > threshold: result.append(i)
        return result
        
# @lc code=end

