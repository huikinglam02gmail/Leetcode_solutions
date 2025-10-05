#
# @lc app=leetcode id=3576 lang=python3
#
# [3576] Transform Array to All Equal Elements
#

from typing import List

# @lc code=start
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        targets = [1, -1]
        canDo = False
        for target in targets:
            multiplier = 1
            flipCount = 0
            for num in nums:
                if multiplier * num != target:
                    multiplier = -1
                    flipCount += 1
                else: multiplier = 1
            canDo = canDo or (flipCount <= k and multiplier == 1) 
        return canDo

# @lc code=end
