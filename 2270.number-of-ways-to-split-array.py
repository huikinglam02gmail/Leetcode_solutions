#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]
        n = len(nums)
        count = 0
        for num in nums: prefix.append(prefix[-1] + num)
        for i in range(1, n):
            if 2 * prefix[i] >= prefix[-1]: count += 1
        return count
# @lc code=end

