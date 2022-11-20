#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        current, stack, result, positive = 0, [], 0, True
        for c in s:
            if c.isdigit():
                current *= 10
                current += int(c)
            elif c == "+" or c == "-" or c == ")":
                if positive: 
                    result += current
                else:
                    result -= current
                current = 0
                if c == "+" or c == "-":
                    positive = (c == "+")
                else:
                    previous_sign = stack.pop()
                    previous_result = stack.pop()
                    if previous_sign:
                        result = int(previous_result) + result
                    else:
                        result = int(previous_result) - result                    
            elif c == "(":
                stack.append(str(result))
                stack.append(positive)
                current, result, positive = 0, 0, True

        if current != 0:
            if positive:
                result += current
            else:
                result -= current
        return result
# @lc code=end

