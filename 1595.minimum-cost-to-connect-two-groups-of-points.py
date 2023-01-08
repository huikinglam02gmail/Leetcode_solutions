#
# @lc app=leetcode id=1595 lang=python3
#
# [1595] Minimum Cost to Connect Two Groups of Points
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    # 1 <= size1, size2 <= 12
    # dp[i][bitmask] =  minimum cost is we have considered left points i: and bitmask tells us the connection status with the right points
    # Becuase we require all points must be connected somehow to the points in opposite group, bitmask = 0 is disallowed.
    # We note that how you connected 1 is separated from how you connected 2, we just add them up
    # When we reach the end, we just find all the unconnected nodes in second group (from mask) and link them to the minimum cost node on the left
    
    @lru_cache(None)
    def dp(self, i, mask):
        if i == len(self.cost):
            result = 0
            for j in range(len(self.cost[0])):
                if mask & (1 << j) == 0:
                    result += self.minCost[j]
        else:
            result = float('inf')
            for j in range(len(self.cost[0])):
                result = min(result, self.cost[i][j] + self.dp(i + 1, mask | (1 << j)))
        return result 

    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        self.cost = cost
        m = len(cost)
        n = len(cost[0])
        self.minCost = [100]*n        
        for j in range(n):
            for i in range(m):
                self.minCost[j] = min(self.minCost[j], cost[i][j])
      
        return self.dp(0,0)
# @lc code=end

