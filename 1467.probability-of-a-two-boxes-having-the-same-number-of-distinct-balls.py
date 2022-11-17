#
# @lc app=leetcode id=1467 lang=python3
#
# [1467] Probability of a Two Boxes Having The Same Number of Distinct Balls
#

# @lc code=start
from functools import lru_cache
from math import comb


class Solution:
    # DP problem
    # dp(i, num1, color1, num2, color2) = number of valid settings, if balls[i:] is left behind to be drawn
    # num1, num2 = numbers of balls inside boxes 1 and 2
    # color1, color2 = number of colors boxes 1 and 2 respectively 
    
    @lru_cache(None)
    def dp(self, i, num1, color1, num2, color2):
        if num1 > self.total // 2:
            return 0
        if num2 > self.total // 2:
            return 0
        if i == len(self.balls):
            if num1 == self.total // 2 and num2 == self.total // 2 and color1 == color2:
                return 1
            else:
                return 0
        result = 0
        for j in range(self.balls[i]+1):
            multiplicity = comb(self.balls[i], j)
            color1_new, color2_new = color1, color2
            if j > 0:
                color1_new += 1
            if self.balls[i] - j > 0:
                color2_new += 1
            result += multiplicity*self.dp(i+1, num1 + j, color1_new, num2 + self.balls[i] - j, color2_new)
        return result

    def getProbability(self, balls: List[int]) -> float:
        self.balls = balls
        self.total = sum(self.balls)
        return self.dp(0,0,0,0,0) / comb(self.total, self.total // 2)

# @lc code=end

