#
# @lc app=leetcode id=1927 lang=python3
#
# [1927] Sum Game
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    The order of "?" does not matter. Only which side it is on and how many "?" each side have do
    And think about it... if it is "?21":"21?", if Alice put "121" into the left, Bob can always put "211" on the right to balance it out. Then it's the difference between number of l and r "?" that matters! 
    let dp(countDiff, sumDiff, turn) = Alice will win given l - r = countDiff, and the leftSum and rightSum diffrence is given by lrDiff, and it's Alice's (0) or Bob's (1) turn
    '''
    @lru_cache(None)
    def dp(self, diff, lrDiff, turn):
        if diff == 1:
            if turn == 0: return True
            else: return not (-9 <= lrDiff <= 0)
        elif diff == -1:
            if turn == 0: return True
            else: return not (0 <= lrDiff <= 9)             
        else:
            if turn == 0:
                result = False
            else:
                result = True
            if diff > 0:
                for j in range(10):
                    if turn == 0:
                        result = result or self.dp(diff - 1, lrDiff + int(j), 1 - turn)
                    else:
                        result = result and self.dp(diff - 1, lrDiff + int(j), 1 - turn)
            else:
                for j in range(10):
                    if turn == 0:
                        result = result or self.dp(diff + 1, lrDiff - int(j), 1- turn)
                    else:
                        result = result and self.dp(diff + 1, lrDiff - int(j), 1- turn)
            return result

    def sumGame(self, num: str) -> bool:
        n, l, r, leftSum, rightSum = len(num), 0, 0, 0, 0
        for i, c in enumerate(num):
            if i < n // 2:
                if c == "?":
                    l += 1
                else:
                    leftSum += int(c)
            else:
                if c == "?":
                    r += 1
                else:
                    rightSum += int(c)

        return self.dp(l - r, leftSum - rightSum, 0)            
        
# @lc code=end

