#
# @lc app=leetcode id=2943 lang=python3
#
# [2943] Maximize Area of Square Hole in Grid
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0
        for key in seen:
            if key - 1 not in seen:
                counter = 0
                current = key
                while current in seen:
                    counter += 1
                    current += 1
                result = max(result, counter)
        return result
    
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        l = min(self.longestConsecutive(hBars), self.longestConsecutive(vBars)) + 1
        return l * l


        
# @lc code=end

