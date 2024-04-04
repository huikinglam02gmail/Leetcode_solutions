#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    '''
    keep track of which level you're at, and the historical max
    '''
    def maxDepth(self, s: str) -> int:
        current_max = 0
        current = 0
        for c in s:
            if c == "(":
                current += 1
                current_max = max(current_max, current)
            elif c == ")":
                current -= 1
        return current_max
# @lc code=end

