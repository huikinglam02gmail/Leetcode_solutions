#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder:
# maintain two different heaps : left: max and right: min heap to accumulate the data and readily pop out the median value
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.small and num >= -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        # balancing
        while abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                heapq.heappush(self.large, - heapq.heappop(self.small))
            else:
                heapq.heappush(self.small, - heapq.heappop(self.large))

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            return (- self.small[0] + self.large[0]) / 2
        else:
            if len(self.small) > len(self.large):
                return - self.small[0]
            else:
                return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

