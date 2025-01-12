#
# @lc app=leetcode id=2580 lang=python3
#
# [2580] Count Ways to Group Overlapping Ranges
#

# @lc code=start
from typing import List


class Solution:
    '''
    Overlapping range must belong to 1 group
    So sort ranges and merge the overlapping ranges
    Ans is 2 ^ (# nonoverlapping range)
    '''
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        nonOverlap = []
        result = 1
        for a, b in ranges:
            if nonOverlap and a <= nonOverlap[-1][1]: nonOverlap[-1][1] = max(b, nonOverlap[-1][1])
            else:
                result *= 2
                result %= 1000000007
                nonOverlap.append([a, b])
        return result
        
# @lc code=end
