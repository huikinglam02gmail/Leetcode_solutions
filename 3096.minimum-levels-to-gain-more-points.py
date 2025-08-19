#
# @lc app=leetcode id=3096 lang=python3
#
# [3096] Minimum Levels to Gain More Points
#

# @lc code=start
from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        prefix = [0]
        for i in possible:
            if i: prefix.append(prefix[-1] + 1)
            else: prefix.append(prefix[-1] - 1)
        for i in range(1, len(prefix) - 1):
            if prefix[i] > prefix[-1] - prefix[i]: return i
        return -1
# @lc code=end

