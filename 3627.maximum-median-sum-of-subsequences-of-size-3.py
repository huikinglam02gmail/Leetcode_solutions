#
# @lc app=leetcode id=3627 lang=python3
#
# [3627] Maximum Median Sum of Subsequences of Size 3
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        dq = deque(nums)
        result = 0
        while dq:
            dq.popleft()
            dq.pop()
            result += dq.pop()
        return result
# @lc code=end

