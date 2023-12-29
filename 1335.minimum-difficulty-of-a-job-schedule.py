#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
from typing import List


class Solution:
    '''
    Hard to come up with the idea
    In previous approaches, the most time consuming part is the k-loop for max(jobDifficulty[i:k]) + dp(k,j-1)
    Here we change the direction of dp
    dp[i][j] = minimum difficulty if the jobs are jobDifficulty[0:i + 1] and j + 1 days is allowed to finish it
    We are looking for dp[n - 1][d - 1]
    The recurrence relation is dp[i][j] = min(max(jobDifficulty[k + 1:i + 1]) + dp[k][j - 1]), k to loop from j - 2 to i - 1
    Let's suppose we maintain a monotonic decreasing stack of jobDifficulty index when we calculate dp[i][j], and stack[-1] = l, and the element left of i larger than jobDifficulty[i] is m, i.e. jobDifficulty[m] > jobDifficulty[i] >= jobDifficulty[l], m < l < i
    When we loop k, we can separate into two scenarios:
    1. j - 2 <= k <= m
    2. m < k < i
    In case 1, max(jobDifficulty[k + 1:i + 1]) = max(jobDifficulty[k + 1:m + 1])
    The expression becomes max(jobDifficulty[k + 1:m + 1]) + dp[k][j - 1]) = dp[m][j]
    Note that the starting point is always j - 2 and does not change with each k-iteration for different i, so we have already calculated dp[m][j] before dp[i][j]
    For case 2, all the ks have jobDifficulty[k] <= jobDifficulty[i]
    So max(jobDifficulty[k + 1:i + 1]) = jobDifficulty[i], and the expression becomes dp[k][j - 1] + jobDifficulty[i], for m < k < i
    Here we still need to scan between m + 1 and i-1. However, this work is already done before
    Specifically, for example, when we consider k = i - 1, it should be at the end of the stack, i.e. l = i - 1
    we pop it out, and want to find dp[i - 1][j - 1] + jobDifficulty[i]
    Is dp[i - 1][j - 1] related to dp[i - 1][j]? It is, because to get at dp[i - 1][j], we have done the same looping from left closest larger index up to i - 2, and the maximum taken is jobDifficulty[i - 1]
    So dp[i][j] = min(dp[i][j], dp[popped][j] - jobDifficulty[j] + jobDifficulty[i]) 
    '''
    
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [float('inf')] * n
        for day in range(d):
            stack, dp_new = [], [0] * n
            for i in range(day, n):
                # In the new day, we just do job i
                if i == 0:
                    dp_new[i] = jobDifficulty[i]
                else:
                    dp_new[i] = dp[i - 1] + jobDifficulty[i] 
                # Try to incorporate more jobs into day i
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    dp_new[i] = min(dp_new[i], dp_new[j] - jobDifficulty[j] + jobDifficulty[i])
                if stack:
                    dp_new[i] = min(dp_new[i], dp_new[stack[-1]])
                stack.append(i)
            dp = dp_new
        return dp[n-1]
# @lc code=end

