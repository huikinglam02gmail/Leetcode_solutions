#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        stack = [ [] for i in range(26)]
        for i in range(len(s)):
            ind = ord(s[i]) - ord('a')
            if len(stack[ind]) == 2:
                keep = stack[ind].pop()
                stack[ind].pop()
                stack[ind].append(keep)
            else:
                stack[ind].append(i)
        return sum(len(x) for x in stack)
# @lc code=end

