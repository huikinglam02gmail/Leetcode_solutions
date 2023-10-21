#
# @lc app=leetcode id=1953 lang=python3
#
# [1953] Maximum Number of Weeks for Which You Can Work
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    1 <= milestones[i] <= 10^9
    we cannot add one by one. But we should notice that if 2 * max(milestone) > sum(milestone), the answer is 2 * (sum(milestone) - max(milestone)) + 1 (like in Example 2)
    else, each member can be paired with one another and the answer is sum(milestone)
    '''
    def numberOfWeeks(self, milestones: List[int]) -> int:
        M, S = 0, 0
        for milestone in milestones:
            M = max(M, milestone)
            S += milestone
        return S if 2 * M <= S else 2 * (S - M) + 1
# @lc code=end

