#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    '''
    Use stack to handle the problem
    Current takes care of the current number
    When we see the first "+" or "-", we put the current number into the stack
    We also append the operator
    Then we clear up current update until we see another operator
    If the priority of the new operator is higher than that on the one at the stack top, we append the current number onto the stack stop with the second operator
    If not we pop the operator from the stack and calculate the current number    
    '''

    def calulation(self, current):
        old_op = self.opStack.pop()
        old_current = self.numStack.pop()
        if old_op == "+":
            current += old_current
        elif old_op == "-":
            current = -current
            current += old_current
        elif old_op == "*":
            current *= old_current
        else:
            current = old_current // current
        return current
   
    def calculate(self, s: str) -> int:
        self.numStack, self.opStack,  current = [], [], 0
        priority = {"+": 0, "-": 0, "*": 1, "/": 1}
        for c in s:
            if c.isdigit():
                current *= 10
                current += int(c)
            elif c in "+-*/":
                while self.opStack and priority[self.opStack[-1]] >= priority[c]:
                    current = self.calulation(current)
                self.numStack.append(current)
                self.opStack.append(c)
                current = 0
        while self.opStack:
            current = self.calulation(current)
        return current
                        
                        
# @lc code=end

