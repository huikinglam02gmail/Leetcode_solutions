#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            stack = []
            operands = "+-*/"
            for i in tokens:
                if i not in operands:
                    stack.append(int(i))
                else:
                    right = stack.pop()
                    left = stack.pop()
                    if i == "+":
                        result = left + right
                    elif i == "-":
                        result = left - right
                    elif i == "*":
                        result = left * right
                    else:
                        if left*right >= 0 or left % right == 0:
                            result = left // right
                        else:
                            result = left // right + 1
                    stack.append(result)
            return stack[0]
# @lc code=end

