#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#

# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit() and stack and not stack[-1].isdigit(): stack.pop()
            else: stack.append(c)
        return "".join(stack)
# @lc code=end

