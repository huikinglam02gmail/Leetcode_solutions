#
# @lc app=leetcode id=2034 lang=python3
#
# [2034] Stock Price Fluctuation 
#

# @lc code=start
import heapq


class StockPrice:
    '''
    update requires a hashTable {timestamp: price}
    current: requires recording the latest time stamp. Get hashTable[latest]
    maximum and minimum: use a max and min heap with the timestamp as element
    '''
    def __init__(self):
        self.latestTime = 0
        self.maxHeap = []
        self.minHeap = []
        self.hashTable = {}

    def update(self, timestamp: int, price: int) -> None:
        self.latestTime = max(self.latestTime, timestamp)
        self.hashTable[timestamp] = price
        heapq.heappush(self.maxHeap, [- price, timestamp])
        heapq.heappush(self.minHeap, [price, timestamp])

    def current(self) -> int:
        return self.hashTable[self.latestTime]

    def maximum(self) -> int:
        while self.maxHeap and self.hashTable[self.maxHeap[0][1]] != - self.maxHeap[0][0]:
            heapq.heappop(self.maxHeap)
        return - self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap and self.hashTable[self.minHeap[0][1]] != self.minHeap[0][0]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

