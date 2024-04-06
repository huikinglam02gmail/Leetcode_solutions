#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    '''
    Keep a stack to find if each parenthesis is valid
    In a stack, we keep the indices of open and close parenthesis [i, 1] or [i,-1]
    When a new parenthesis come in, we ask if it can close previous open parenthesis that results in a pop. The successful closes will be recorded as good parenthesis    
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, good = [], set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append([i, 1])
            elif c == ")":
                if stack and stack[-1][1] == 1:
                    item = stack.pop()
                    good.add(item[0])
                    good.add(i)
                else:
                    stack.append([i, -1])
        result = ""
        for i, c in enumerate(s):
            if c.isalpha() or i in good:
                result += c
        return result
# @lc code=end

