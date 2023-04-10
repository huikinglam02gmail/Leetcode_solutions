#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")","[":"]","{":"}"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif len(stack) > 0:
                if c == pairs[stack[-1]]: 
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
    
# @lc code=end

