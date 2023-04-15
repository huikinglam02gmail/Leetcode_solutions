from typing import List


class Solution:
    '''
    Think about it in DP. Suppose we only have piles[0]. Then to get k coins (assuming k <= len(piles[0])), we just add piles[0][:k]
    Now suppose we introduce piles[1]. Then we have to consider among k, we take i from piles[1] and k - i piles from piles[:1]
    dp[i][j] =  maximum total value of coins you can have in your wallet if you choose exactly j coins optimally, given you are given piles[:i + 1].
    '''
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = {0: 0}
        for i in range(n):
            dpNew = {}
            prefixSum = 0       
            for j in range(len(piles[i]) + 1):
                for key, value in dp.items():
                    if key + j <= k:
                        if key + j not in dpNew:
                            dpNew[key + j] = value + prefixSum
                        else:
                            dpNew[key + j] = max(dpNew[key + j], value + prefixSum)
                if j < len(piles[i]):
                    prefixSum += piles[i][j]
            dp = dpNew
        return dp[k]
    