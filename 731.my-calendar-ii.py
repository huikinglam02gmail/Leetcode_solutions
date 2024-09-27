#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
import bisect


class MyCalendarTwo(object):
    '''
    Boundary counting to detect overlaps
    Start and end are treated as +1 and -1
    Maintain a sorted list of time point
    At each time point, insert into the sorted list and traverse once through the list to test whether we see the sum goings above 2    
    '''


    def __init__(self):
        self.record = []

    def book(self, start, end):
        if not self.record:
            self.record.append([start, 1])
            self.record.append([end, -1])
            return True

        bisect.insort(self.record,[start,1])
        bisect.insort(self.record,[end, -1])
        
        booked = 0
        for k in range(len(self.record)):
            booked += self.record[k][1]
            if booked == 3:
                self.record.remove([start, 1])
                self.record.remove([end, -1])
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

