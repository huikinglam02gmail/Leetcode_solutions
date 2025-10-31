#
# @lc app=leetcode id=3727 lang=python3
#
# [3727] Maximum Alternating Sum of Squares
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [num * num for num in nums]
        nums.sort()
        dq = deque(nums)
        result = 0
        while dq:
            result += dq.pop()
            if dq: result -= dq.popleft()
        return result

# @lc code=end
