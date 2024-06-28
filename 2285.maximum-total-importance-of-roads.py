#
# @lc app=leetcode id=2285 lang=python3
#
# [2285] Maximum Total Importance of Roads
#

# @lc code=start
from typing import List


class Solution:
    '''
    Each city[i] will contribute final assignent num * degree[i] to the total. Therefore, just count degree, sort degree from high to low, and add
    '''
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1
        degrees.sort()
        result = 0
        for i in range(n): result += (i + 1) * degrees[i]
        return result
# @lc code=end

