#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

