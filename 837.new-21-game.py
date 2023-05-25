#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    '''
    DP problem
    Define dp[i] = probability of getting i point
    To get at i point, we need to come from i - x, in which dp[i] += dp[i-x] / maxPts
    We stop this procedure when i >= k
    When one look at the recurrence relation, we see that keeping a sliding window will be a good idea    
    '''

    def new21Game(self, n: int, k: int, maxPts: int) -> float:        
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        window_sum = 0
        for i in range(1, n + 1):
            if maxPts < i < k + 1 + maxPts:
                window_sum -= dp[i - maxPts - 1]
            if i < k + 1:
                window_sum += dp[i - 1]
            dp[i] += window_sum / maxPts
        return sum(dp[k:])
# @lc code=end

