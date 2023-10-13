#
# @lc app=leetcode id=1943 lang=python3
#
# [1943] Describe the Painting
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    end <= 100000
    We can do a line sweep from left to right. 
    First sort by segments start. 
    For each coordinate, ask if there are any ends ending at it. If so, update the last element in result, together with the color. When encounter a new segment, i >= segment[0], we put the [right, color] into a min heap, and add [segment[0], i, cumu]
    '''
    def endOldSegment(self, i, totalColor):
        if self.result:
            self.result[-1][1] = i
            self.result[-1][2] = totalColor

    def addNewSegment(self, i):
        self.result.append([i, -1, -1])

    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        exit, self.result = [], []
        cumu, segmentPtr = 0, 0
        segments.sort()
        limit = max([x[1] for x in segments])
        for i in range(1, limit + 1):
            countSameEnd = 0
            while exit and exit[0][0] == i:
                end, color = heapq.heappop(exit)
                countSameEnd += 1
                if countSameEnd == 1:
                    self.endOldSegment(i, cumu)
                    self.addNewSegment(i)
                cumu -= color

            countSameStart = 0
            while segmentPtr < len(segments) and segments[segmentPtr][0] == i:
                heapq.heappush(exit, [segments[segmentPtr][1], segments[segmentPtr][2]])
                countSameStart += 1
                if countSameStart == 1:
                    if cumu > 0 and self.result[-1][0] != i:
                        self.endOldSegment(i, cumu)
                        self.addNewSegment(i)
                    elif self.result:
                        self.result[-1][0] = i
                    else:
                        self.addNewSegment(i)
                cumu += segments[segmentPtr][2]
                segmentPtr += 1
        self.result.pop()
        return self.result

# @lc code=end

