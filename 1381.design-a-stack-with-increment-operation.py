#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:
    '''
    Use a stack to maintain the stack
    Use a second increment stack to maintain the increment at the each index
    add the value to the value to be returned, and pass on to smaller indices    
    '''
    def __init__(self, maxSize: int):
        self.stack, self.inc = [], []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)
        
    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1: self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()
                        
    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k, len(self.inc))-1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

