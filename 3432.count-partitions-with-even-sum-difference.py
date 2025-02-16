#
# @lc app=leetcode id=3432 lang=python3
#
# [3432] Count Partitions with Even Sum Difference
#

# @lc code=start
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums: prefix.append(prefix[-1] + num)
        result = 0
        for i in range(1, len(prefix) - 1):
            if abs(prefix[-1] - 2 * prefix[i]) % 2 == 0: result += 1
        return result
# @lc code=end

