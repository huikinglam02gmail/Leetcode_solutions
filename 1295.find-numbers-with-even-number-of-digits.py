#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0: result += 1
        return result
# @lc code=end

