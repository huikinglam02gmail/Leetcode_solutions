#
# @lc app=leetcode id=1896 lang=python3
#
# [1896] Minimum Cost to Change the Final Value of Expression
#

# @lc code=start
class Solution:
    '''
    Notice the rules:
    '&' does not take precedence over '|' in the order of calculation.
    Evaluate parentheses first, then in left-to-right order.
    So first deal with parentheses first, use stack to hold the calculated expression
    When we calculate, we record what the original value is. And the minimum cost to flip it to 1 - value
    Because parentheses can occur on the RHS, we have these scenarios:
    exp1 op exp2
    1. 0 & 0 -> 1 + min(cost(exp1), cost(exp2))
    2. 0 | 0 -> min(cost(exp1), cost(exp2))
    3. 0 & 1 -> 1
    4. 0 | 1 -> 1
    5. 1 & 0 -> 1
    6. 1 | 0 -> 1
    7. 1 & 1 -> min(cost(exp1), cost(exp2))
    8. 1 | 1 -> 1 + min(cost(exp1), cost(exp2))   
    '''
    def flipCost(self, left, op, right):
        if op == '!':
            return right
        else:
            if op == '&':
                newValue = int((left[0] > 0) and (right[0] > 0))
            else:
                newValue = int((left[0] > 0) or (right[0] > 0))
            if left[0] != right[0]:
                newCost = 1
            else:
                newCost = min(left[1], right[1])
                if (op == '&' and left[0] == 0) or (op == '|' and left[0] == 1):
                    newCost += 1
            return [newValue, newCost]


    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        stackOp = []
        current = [-1, 0]
        currentOp = '!'
        for c in expression:
            if c == '&' or c == '|':
                currentOp = c
            elif c == '(':
                stack.append(current)
                stackOp.append(currentOp)
                current = [-1, 0]
                currentOp = '!'
            elif c == ')':
                leftTuple = stack.pop()
                leftOp = stackOp.pop()
                current = self.flipCost(leftTuple, leftOp, current)
            else:
                current = self.flipCost(current, currentOp, [int(c), 1])
        return current[1]
        
# @lc code=end

