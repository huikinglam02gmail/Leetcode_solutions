#
# @lc app=leetcode id=1665 lang=python3
#
# [1665] Minimum Initial Energy to Finish Tasks
#

# @lc code=start
from typing import List


class Solution:
    '''
    We should first do the jobs with more excess between minimum and actual. The saved effort can be used to fund the remaining tasks
    '''
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1])
        result, store = 0, 0
        for act, min in tasks:
            supply = max(0, min - store)
            result += supply
            store += supply - act
        return result
# @lc code=end

