#
# @lc app=leetcode id=3153 lang=python3
#
# [3153] Sum of Digit Differences of All Pairs
#

# @lc code=start
from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(str(nums[0]))
        counts = [[0] * 10 for _ in range(n)]
        for num in nums:
            for i, ch in enumerate(str(num)):
                counts[i][int(ch)] += 1
        result = 0
        for count in counts:
            for i in range(9):
                for j in range(i + 1, 10):
                    result += count[i] * count[j]
        return result
# @lc code=end

