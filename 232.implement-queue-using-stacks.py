#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    # Two stacks are used
    # stack1 is for holding elements that is pushed
    # When pop is called, the elements in stack1 is popped in reverse order of they are pushed. They are appended to stack2 one by one. So on another popping, FIFO is achieved
    # 
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def clearance(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self) -> int:
        self.clearance()
        return self.stack2.pop()
    
    def peek(self) -> int:
        self.clearance()
        return self.stack2[-1]
        
    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

