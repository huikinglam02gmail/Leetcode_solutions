#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    First get all the numbers and sort them.
    We can cut short and return -1 if (nums[i] - nums[0]) % x != 0, and totally skip this check if x == 1
    Then the final answer is the median of the array
    '''
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        nums.sort()
        if x > 1:
            for i in range(1, m * n, 1):
                if (nums[i] - nums[0]) % x: return -1
        result = 0
        for num in nums: result += abs(num - nums[m * n // 2]) // x
        return result
        
# @lc code=end

