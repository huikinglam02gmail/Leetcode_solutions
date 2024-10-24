#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 if num % 3 else 0 for num in nums])
# @lc code=end

