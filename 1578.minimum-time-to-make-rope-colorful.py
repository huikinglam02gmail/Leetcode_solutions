#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start
from typing import List


class Solution:
    '''
    We only need to concern about CONSECUTIVE same color
    Therefore, we just need to look at consecutive streaks: sum consecutive same streak up and also take note of the maximum seen so far
    result += total - max    
    '''
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, j, result, n = 0, 0, 0, len(colors)
        while i < n and j < n:
            S, m = 0, 0
            while j < n and colors[j] == colors[i]:
                S += neededTime[j]
                m = max(m, neededTime[j])
                j += 1
            result += S - m
            i = j
        return result
# @lc code=end

