#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
from collections import deque
import heapq


class Solution:
    '''
    For each index i, if s[i] = "0", and i is within the active range, we can add[i + minJump, i + maxJump] into the active range. 
    Because minJump and maxJump is the same for every i, we know the smallest start is the smallest end.
    To maintain the active range, we can use a deque of end.
    When we arrive at each i, we pop all active range with end < i.
    Then we check if s[i] == '0'. If so, we ask if start <= i <= end  
    '''

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dq = deque()
        dq.append(0)
        result = False
        for i, c in enumerate(s):
            while dq and dq[0] < i:
                dq.popleft()
            if c == '0' and dq and dq[0] - maxJump + minJump <= i <= dq[0]:
                dq.append(i + maxJump)
                if i == len(s) - 1:
                    result = True
        return result
# @lc code=end

