#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
from typing import List


class Solution:
    # First record appearance of each difficulty level
    # Then dp from 1 to maxValue
    
    def minimumRounds(self, tasks: List[int]) -> int:
        hashTable = {}
        for task in tasks:
            if task not in hashTable:
                hashTable[task] = 0
            hashTable[task] += 1
        maxValue = max(hashTable.values())
        dp = [0]*(maxValue + 1)
        dp[1] = float('Inf')
        for i in range(2, maxValue + 1):
            dp[i] = 1
            if i >= 4:
                dp[i] += min(dp[i - 2], dp[i - 3])
        result = 0
        for v in hashTable.values():
            result += dp[v]
        if result == float('Inf'):
            return -1
        else:
            return result
# @lc code=end

