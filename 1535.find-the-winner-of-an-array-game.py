#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game
#

# @lc code=start
class Solution:
    # the maximum element will take at most n - 1 rounds to reach the 0th position
    # otherwise, just simulate
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arrMax = max(arr)
        if k >= n:
            return max(arr)
        stack = []
        while arr:
            stack.append(arr.pop())
        win = 0
        while win < k and stack[-1] < arrMax:
            last = stack.pop()
            secondLast = stack.pop()
            if last > secondLast:
                win += 1
                stack.append(last)
            else:
                win = 1
                stack.append(secondLast)
        return stack[-1]
# @lc code=end

