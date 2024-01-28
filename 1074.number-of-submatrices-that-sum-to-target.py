#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

# @lc code=start
from typing import List


class Solution:
    '''
    2D version of Leetcode 560. Subarray Sum Equals K
    The idea is the same. Calculate prefix sums row by row first
    Then for each columns pair (i,j), add the prefix sum differences row by row
    In each row, ask if new sum - target was seen before    
    '''
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_sums = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sums[i][j] = matrix[i - 1][j - 1]
                if j > 1: prefix_sums[i][j] += prefix_sums[i][j - 1]
        
        result = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                cumu_sum_seen, cumu_sum = {0: 1}, 0
                for row in range(1, m + 1):
                    cumu_sum += prefix_sums[row][j] - prefix_sums[row][i]
                    if cumu_sum - target in cumu_sum_seen:
                        result += cumu_sum_seen[cumu_sum - target]
                    cumu_sum_seen[cumu_sum] = cumu_sum_seen.get(cumu_sum, 0) + 1
        return result
            
# @lc code=end

