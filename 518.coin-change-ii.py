#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from typing import List


class Solution:
    '''
    simple dp. dp[i] = number of ways to reach i. given each coin, we just increment the i + coin which range between 0 and amount - coin
    '''

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1 - coin):
                dp[i + coin] += dp[i]
        return dp[amount]

# @lc code=end

