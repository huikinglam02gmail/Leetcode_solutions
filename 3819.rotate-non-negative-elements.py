#
# @lc app=leetcode id=3819 lang=python3
#
# [3819] Rotate Non Negative Elements
#

# @lc code=start
from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        indicesToRotate = []
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if num >= 0:
                indicesToRotate.append(i)
            else:
                result[i] = num
        for i, ind in enumerate(indicesToRotate):
            finalPosition = (i - k) % len(indicesToRotate)
            result[indicesToRotate[finalPosition]] = nums[ind]
        return result
# @lc code=end

