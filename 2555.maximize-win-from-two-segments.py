#
# @lc app=leetcode id=2555 lang=python3
#
# [2555] Maximize Win From Two Segments
#

# @lc code=start
import bisect
from collections import deque
import heapq
from typing import List


class Solution:
    '''
    Always optimal to start from two indices without overlap
    '''
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        if prizePositions[-1] - prizePositions[0] <= 2 * k: return len(prizePositions)
        result = 0
        positions = sorted(set(prizePositions))
        maxSoFar = 0
        dq = deque()
        for pos in positions:
            while dq and dq[0][0] + k < pos:
                start, prize = dq.popleft()
                maxSoFar = max(maxSoFar, prize)
            total = bisect.bisect_right(prizePositions, pos + k) - bisect.bisect_left(prizePositions, pos)
            result = max(result, total + maxSoFar)
            dq.append([pos, total])
        return result
            

# @lc code=end

