#
# @lc app=leetcode id=1326 lang=python3
#
# [1326] Minimum Number of Taps to Open to Water a Garden
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        heap = []
        candidates = [[i - r, i + r] for i, r in enumerate(ranges)]
        candidates.sort()

        result, cur, i = 0, 0, 0
        while cur < n:
            while i < len(candidates) and cur >= candidates[i][0]:
                heapq.heappush(heap, - candidates[i][1])
                i += 1
            if heap and - heap[0] > cur:
                cur = - heap[0]
                result += 1
            else:
                return -1
        return result
# @lc code=end

