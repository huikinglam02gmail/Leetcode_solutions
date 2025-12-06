#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#

# @lc code=start
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        data = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                data.append(grid[i][j])
        self.MOD = 12345
        
        dataFlattened = self.productExceptSelf(data)
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = dataFlattened[i * n + j]
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for i in range(n)]
        
        for i in range(1, n, 1):
            result[i] = result[i - 1] * nums[i - 1]
            result[i] %= self.MOD
        last = nums[-1]
        for i in range(n - 2, -1, -1):
            result[i] *= last
            result[i] %= self.MOD
            last *= nums[i]
            last %= self.MOD
        return result
# @lc code=end

