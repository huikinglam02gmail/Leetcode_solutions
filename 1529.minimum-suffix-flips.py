#
# @lc app=leetcode id=1529 lang=python3
#
# [1529] Minimum Suffix Flips
#

# @lc code=start
class Solution:
    # Do the flip from left to right
    # a Flip is needed whenever we see a transition
    def minFlips(self, target: str) -> int:
        prev, result = '0', 0
        for c in target:
            if c != prev:
                result += 1
                prev = c
        return result
# @lc code=end

