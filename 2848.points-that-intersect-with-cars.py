#
# @lc app=leetcode id=2848 lang=python3
#
# [2848] Points That Intersect With Cars
#
from typing import List

# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        end = 0
        count = 0
        for start, finish in nums:
            if start > end:
                count += finish - start + 1
                end = finish
            else:
                count += max(0, finish - end)
                end = max(end, finish)
        return count
# @lc code=end

