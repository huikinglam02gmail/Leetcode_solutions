#
# @lc app=leetcode id=1690 lang=python3
#
# [1690] Stone Game VII
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    2 <= n <= 1000, n^2 algorithm is acceptable
    dp(i, j, t) = optimal score difference if stones[i:j] is left behind, and t = 1 if it's Alice's turn, -1 if it's Bob's turn
    We are interested to get dp(0, n, 1).
    To get the sum quickly, we prepare prefix sum
    Boundary conditions: 
    dp(i, i + 1, t) = 0
    dp(i, j, t) = max(t*sum(stones[i:j-1]) + dp(i, j - 1, -t), t*sum(stones[i+1:j]) + dp(i + 1, j, -t)))
    '''
    def dp(self, i, j):
        if (i,j) in self.memo:
            return self.memo[(i, j)]
        elif j == i + 1:
            return 0
        else:
            result = max(self.prefix[j - 1] - self.prefix[i] - self.dp(i, j - 1), self.prefix[j] - self.prefix[i + 1] - self.dp(i + 1, j))
            self.memo[(i, j)] = result
            return result
    
    def stoneGameVII(self, stones: List[int]) -> int:
        self.prefix = [0]
        n = len(stones)
        self.memo = {}
        for stone in stones:
            self.prefix.append(self.prefix[-1] + stone)
        return self.dp(0, n)
# @lc code=end

