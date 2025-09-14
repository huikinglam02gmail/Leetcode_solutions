#
# @lc app=leetcode id=3683 lang=python3
#
# [3683] Earliest Time to Finish One Task
#

# @lc code=start
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([s + t for s, t in tasks])
# @lc code=end

