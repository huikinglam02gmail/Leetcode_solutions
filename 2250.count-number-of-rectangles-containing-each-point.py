#
# @lc app=leetcode id=2250 lang=python3
#
# [2250] Count Number of Rectangles Containing Each Point
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    1 <= li, xj <= 10^9
    1 <= hi, yj <= 100
    height is limited, so we can store rectangles as [[x sorted] for j in range(100)]
    Then given each point, we conduct binary search for j <= yj
    '''
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rects = [[] for j in range(101)]
        rectangles.sort()
        for l, h in rectangles: rects[h].append(l)
        result = []
        for x, y in points:
            count = 0
            for j in range(y, 101, 1): count += len(rects[j]) - bisect.bisect_left(rects[j], x)
            result.append(count)
        return result
# @lc code=end

