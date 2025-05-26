#
# @lc app=leetcode id=3561 lang=python3
#
# [3561] Resulting String After Adjacent Removals
#

# @lc code=start
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and (abs((ord(c) - ord(stack[-1]))) == 1 or abs((ord(c) - ord(stack[-1]))) == 25):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
# @lc code=end

