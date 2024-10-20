#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#

# @lc code=start
class Solution:
    '''
    We have 3 operators: !, & and |
    And I checked, !&(t,f) is not an invalid input but !(&(t,f)) is
    Also, "|(f,t)&(t,f)" gives true, meaning the testcases would be focusing on only the first segment and will not ask you to compute logical operations on 2 or more segments
    I will use stack as usual to handle the brackets
    Because of the presence of ",", we should use two lists prev and current to store the state
    So the rules are:
    if we see "!", state = 0
    if we see "&", state = 1
    if we see "|", state = 2
    If we see alphabets, adjust the current states
    if we see ",", we pop current and operate on what's inside prev (state is given by stack[-1])
    if we see "(": append prev into the stack, set prev to be empty, append the state to the stack as well
    if we see ")", we pop the current state from stack
    Then we pop the previous prev (prevprev) from stack and operate prev onto prevprev and assign prevprev to prev     
    '''

    def parseBoolExpr(self, expression: str) -> bool:
        stack, prev, current, state = [], [], True, -1
        for c in expression:
            if c == "t": current = True
            if c == "f": current = False
            if c == "!": state = 0
            if c == "&": state = 1
            if c == "|": state = 2
            if c == "," or c == ")":
                if not prev:
                    if stack[-1] > 0: prev.append(current)
                    else: prev.append(not current)
                elif stack[-1] == 1: prev[0] &= current
                elif stack[-1] == 2: prev[0] |= current
            if c == "(":
                stack.append(prev)
                prev = []
                stack.append(state)
            if c == ")":
                old_state = stack.pop()
                prev, current = stack.pop(), prev[0]
        return current
                
                
# @lc code=end

