#
# @lc app=leetcode id=2526 lang=python3
#
# [2526] Find Consecutive Integers from a Data Stream
#

# @lc code=start
from collections import deque


class DataStream:

    def __init__(self, value: int, k: int):
        self.dq = deque()
        self.value = value
        self.k = k
        self.hashTable = {}

    def consec(self, num: int) -> bool:
        self.hashTable[num] = self.hashTable.get(num, 0) + 1
        self.dq.append(num)
        while len(self.dq) > self.k: self.hashTable[self.dq.popleft()] -= 1
        return num == self.value and self.hashTable[num] == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
# @lc code=end

