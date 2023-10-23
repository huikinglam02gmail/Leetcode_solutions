#
# @lc app=leetcode id=1955 lang=python3
#
# [1955] Count Number of Special Subsequences
#

# @lc code=start
from typing import List


class Solution:
    '''
    Let dp[i][j] = number of subsequences ending with j when we are given nums[:i + 1]
    We want to get dp[-1][2]
    '''
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        prev = [0, 0, 0]
        MOD = pow(10, 9) + 7
        for num in nums:
            nxt = [0, 0, 0]
            for i in range(3):
                nxt[i] += prev[i]
                if i == num:
                    nxt[i] += prev[i]
                    if i > 0:
                        nxt[i] += prev[i - 1]
                nxt[i] %= MOD 
            if num == 0:
                nxt[num] += 1
            prev = nxt
        return prev[-1]
        
# @lc code=end

