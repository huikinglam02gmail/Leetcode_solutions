#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
import bisect
from operator import itemgetter


class MyCalendar:
    '''
    Simpler than range module problem
    In here we keep a nonoverlapping sorted intervals
    When a new interval comes (start, end), we binary search start against the interval ends to locate which position it would fit. Also, we binary search end against the interval starts. We also update the intervals if we found a fit
    1. li == ri: we've got perfect insertion into li index, no overlap with other intervals
    2. li == ri - 1: it must be either end is touching start of another interval or start is touching end of another interval
    3. li == ri - 2: it must be start and end are overlapping with start and end of two neighboring intervals    
    '''
    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if not self.intervals:
            self.intervals.append([start, end])
            return True
        else:
            li = bisect.bisect_left(self.intervals, start, key = itemgetter(1))
            ri = bisect.bisect_right(self.intervals, end, key = itemgetter(0))
            if ri - li > 2: return False
            elif ri == li + 2:
                if end != self.intervals[ri-1][0] or start != self.intervals[li][1]: return False
                self.intervals[li:ri] = [[self.intervals[li][0], self.intervals[ri-1][1]]]
            elif ri == li + 1:
                if end != self.intervals[li][0] and start != self.intervals[li][1]: return False
                if end == self.intervals[li][0]: self.intervals[li][0] = start
                else: self.intervals[li][1] = end
            else:
                self.intervals[li: ri] = [[start, end]]
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

