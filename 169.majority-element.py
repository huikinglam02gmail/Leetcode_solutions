#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0
        for num in nums:
            if (votes == 0):
                candidate = num
                votes = 1
            else:
                if (num == candidate):
                    votes += 1
                else:
                    votes -= 1
        return candidate
# @lc code=end

