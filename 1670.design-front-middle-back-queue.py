#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque


class FrontMiddleBackQueue:
    '''
    Use two queues. Always keep the right queue at most 1 element longer than the left queue. 
    '''

    def __init__(self):
        self.left = deque()
        self.right = deque()
    
    def balance(self):
        while len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        while len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        self.left.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        result = - 1
        if self.left:
            result = self.left.popleft()
            self.balance()
        elif self.right:
            result = self.right.popleft()
            self.balance()
        return result

    def popMiddle(self) -> int:
        result = -1
        if len(self.left) == len(self.right) and len(self.right):
            result = self.left.pop()
            self.balance()
        elif len(self.left) < len(self.right) and len(self.right) > 0:
            result = self.right.popleft()
            self.balance()
        return result       

    def popBack(self) -> int:
        result = -1
        if self.right:
            result = self.right.pop()
            self.balance()
        return result


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end
