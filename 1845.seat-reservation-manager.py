#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
import heapq


class SeatManager:
    '''
    want smallest number from unreserved seat: use min heap
    For each call to unreserve, it is guaranteed that seatNumber will be reserved -> no need to keep track of reserved seat
    '''

    def __init__(self, n: int):
        self.free = []
        for i in range(1, n + 1, 1):
            heapq.heappush(self.free, i)
            
    def reserve(self) -> int:
        return heapq.heappop(self.free)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.free, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

