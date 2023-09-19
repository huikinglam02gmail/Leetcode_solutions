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
    dp[bitmask] = [tEarliest, tLatest] the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively, if the 
    '''
    @lru_cache(None)
    def dp(self, mask, round):
        l, r, newMask, step = 0, self.n - 1, 0, 0
        while mask & (1 << l) == 0:
            l += 1
        while mask & (1 << r) == 0:
            r += 1

        result = [float("inf"), 0]

        dq = deque()
        dq.append([newMask, l, r])

        while dq:
            for i in range(len(dq)):
                bitMask, l, r = dq.popleft()
                if l == r:
                    newMask = bitMask ^ (1 << l)

                if l == self.firstPlayer - 1 and r == self.secondPlayer - 1:
                    result[0] = min(result[0], round + step)
                    result[1] = max(result[1], round + step)
                    return result
                elif l == self.firstPlayer:
                    newMask += (1 << l)
                    l += 1
                elif r == self.secondPlayer:
                    newMask += (1 << r)
                    r -= 1
                else:



    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        self.n = n
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer
        
        dq = deque()
        dq.append([1 << (self.n) - 1])
        roundId = 1
        while dq:
            for i in range(len(dq)):
                mask = dq.popleft()
                newMask = 0
                if (left == self.firstPlayer and right == self.secondPlayer) or (left == self.secondPlayer and right == self.firstPlayerPlayer):
                    dp[0] = min(dp[0], roundId)

        return dp[(1 << self.n) - 1]
        
# @lc code=end

