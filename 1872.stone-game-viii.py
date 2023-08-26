#
# @lc app=leetcode id=1872 lang=python3
#
# [1872] Stone Game VIII
#

# @lc code=start
from typing import List


class Solution:
    '''
    A DP problem
    dp[i] =  maximum score difference when stones[:i + 1] was taken, and it is Alice's turn. 
    dp[i] = max(sum(stones[:j + 1]) - dp[j]) for j > i
    We notice this sounds like a O(n^2) algorithm, but notice when only j appears on the rhs, and if j > i, j > i - 1...
    '''
    def stoneGameVIII(self, stones: List[int]) -> int:
        dp = sum(stones)
        total = dp
        n = len(stones)
        for i in range(n - 2, 0, -1):
            total -= stones[i + 1]
            dp = max(dp, total - dp)
        return dp

# @lc code=end

