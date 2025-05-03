#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
from typing import List


class Solution:
    '''
    Cases in which this would not work:
    at least one of i out of (1-6) must be present at every domino
    with each candidates, we can find the number of steps to get top filled with the candidate. The result would be minimum of (steps, n - steps)     
    '''
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = float("inf")
        for i in range(6):
            current = [0, 0]
            for j in range(len(tops)):
                if bottoms[j] == i + 1 and tops[j] != i + 1: current[0] += 1
                elif tops[j] == i + 1 and bottoms[j] != i + 1: current[1] += 1
                elif tops[j] != i + 1 and bottoms[j] != i + 1:
                    current[0] = float("inf")
                    current[1] = float("inf")
            result = min(result, current[0], current[1])
        return result if result != float("inf") else -1


# @lc code=end

