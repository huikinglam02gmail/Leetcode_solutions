#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game
#

# @lc code=start
from typing import List


class Solution:
    '''
    the maximum element will take at most n - 1 rounds to reach the 0th position
    otherwise, just simulate       
    '''
    def getWinner(self, arr: List[int], k: int) -> int:
        stack = []
        arrMax = 0
        while arr:
            stack.append(arr.pop())
            arrMax = max(arrMax, stack[-1])
        if k >= len(stack): return arrMax
        win = 0
        while win < k and stack[-1] < arrMax:
            last = stack.pop()
            secondLast = stack.pop()
            if last <= secondLast: win = 0
            win += 1
            stack.append(max(last, secondLast))
        return stack[-1]
# @lc code=end

