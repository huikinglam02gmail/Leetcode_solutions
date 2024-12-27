#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
from typing import List


class Solution:
    '''
    Looks hard, always remember dp (structured brute force)!
    Score between pair (i,j) (i < j) = values[i] + values[j] - (j - i)
    dp[j] = max score of pairs (0:j - 1, j)
    dp[j + 1] = max(dp[j] - values[j] + values[j + 1] - 1, values[j] + values[j + 1] - 1) 
    '''

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n, max_so_far = len(values), 0
        for i in range(1, n):
            curr = values[i - 1] + values[i] - 1
            if i > 1: curr = max(curr, last - values[i - 1] + values[i] - 1)
            last = curr
            max_so_far = max(max_so_far, last)
        return max_so_far
# @lc code=end

