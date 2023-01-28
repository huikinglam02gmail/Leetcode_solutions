#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start

import bisect
from operator import itemgetter
from typing import List


class SummaryRanges:
    # 
    def __init__(self):
        self.intervals = []
        self.appear = set()

    def addNum(self, value: int) -> None:
        if value not in self.appear:
            self.appear.add(value)
            ind = bisect.bisect_left(self.intervals, value, key = itemgetter(0))
            if value - 1 in self.appear and value + 1 in self.appear:
                self.intervals[ind - 1][1] = self.intervals[ind][1]
                self.intervals.pop(ind)
            elif value - 1 in self.appear:
                self.intervals[ind - 1][1] = value
            elif value + 1 in self.appear:
                self.intervals[ind][0] = value
            else:
                self.intervals.insert(ind, [value, value])


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end

