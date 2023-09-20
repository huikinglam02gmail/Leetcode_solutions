#
# @lc app=leetcode id=1900 lang=python3
#
# [1900] The Earliest and Latest Rounds Where Players Compete
#

# @lc code=start
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    '''
    dp[bitmask] = [tEarliest, tLatest] the earliest possible round and the latest possible round in which these two players will compete against each other, respectively.
    For each bitmask, we find it's boundary 1s.
    Since firstPlayer < secondPlayer, there are 4 cases:
    1. l = firstPlayer and r = secondPlayer: return [1, 1]
    2. l = firstPlayer: l move to next round
    3. r = secondPlayer: r move to next round
    4. both of them are not firstPlayer and secondPlayer: consider both
    '''
    @lru_cache(None)
    def dp(self, competitors, winners, round):
        result = [float("inf"), 0]
        if competitors == 0:
            result = self.dp(winners, 0, round + 1)
        else:
            l, r = 0, self.n - 1
            while l < self.n and (competitors & (1 << l)) == 0:
                l += 1
            while r >= 0 and (competitors & (1 << r)) == 0:
                r -= 1
            
            competitors ^= (1 << l)
            if l < r:
                competitors ^= (1 << r)
            if l == self.firstPlayer - 1 and r == self.secondPlayer - 1:
                result = [round, round]
            elif l == self.firstPlayer - 1 or l == self.secondPlayer - 1:
                result = self.dp(competitors, winners ^ (1 << l), round)
            elif r == self.firstPlayer - 1 or r == self.secondPlayer - 1:
                result = self.dp(competitors, winners ^ (1 << r), round)
            else:
                leftWins = self.dp(competitors, winners ^ (1 << l), round)
                rightWins = self.dp(competitors, winners ^ (1 << r), round)
                result = [min(leftWins[0], rightWins[0]), max(leftWins[1], rightWins[1])]
        return result


    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        self.n = n
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer

        return self.dp((1 << self.n) - 1, 0, 1)
        
# @lc code=end

