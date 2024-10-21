#
# @lc app=leetcode id=3300 lang=python3
#
# [3300] Minimum Element After Replacement With Digit Sum
#

# @lc code=start
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([sum(int(c) for c in str(num)) for num in nums])
# @lc code=end

