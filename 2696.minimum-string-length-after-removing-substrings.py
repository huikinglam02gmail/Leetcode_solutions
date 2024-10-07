#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    '''
    Use a stack
    '''
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and ((c == "B" and stack[-1] == "A") or (c == "D" and stack[-1] == "C")): stack.pop()
            else: stack.append(c)
        return len(stack)
# @lc code=end

