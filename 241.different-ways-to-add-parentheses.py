#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
from typing import List


class Solution:
    '''
    # of parentheses pair = number of operators
    dp[i][j] = [possible results give numbers[i:j+1] and the operators within]
    '''
    def math(self, x, y, op):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        numbers = []
        operators = []
        appeared = False
        current = ""
        for c in expression:
            if c.isdigit():
                if appeared:
                    numbers.append(int(current))
                    appeared = False
                    current = ""
                current = current + c
            else:
                operators.append(c)
                appeared = True
        numbers.append(int(current))
        
        dp = [[[] for i in range(len(numbers))] for j in range(len(numbers))]
        for i in range(len(dp)):
            dp[i][i] = [numbers[i]]
        for j in range(1,len(dp)):
            for i in range(j-1,-1,-1):
                for k in range(j):
                    for l in dp[i][k]:
                        for m in dp[k+1][j]:
                            dp[i][j].append(self.math(l,m,operators[k]))
        return dp[0][-1]
# @lc code=end

