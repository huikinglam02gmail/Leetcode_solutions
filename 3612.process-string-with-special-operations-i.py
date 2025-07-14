#
# @lc app=leetcode id=3612 lang=python3
#
# [3612] Process String with Special Operations I
#

# @lc code=start
class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if stack: stack.pop()
            elif c == "#": stack = stack + stack
            elif c == "%": stack.reverse()
            else: stack.append(c)
        return "".join(stack)
# @lc code=end

