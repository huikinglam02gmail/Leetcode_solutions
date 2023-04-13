#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just simulate, no need figure out the possible ways
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, n, j = [], len(pushed), 0
        for num in pushed:
            if num != popped[j]:
                stack.append(num)
            else:
                j += 1
                while stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
        return j == n
# @lc code=end

