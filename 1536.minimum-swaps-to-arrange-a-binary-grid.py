#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #summarizing row into number 
        row = [-1]*n 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] = j
        ans = 0
        #sequentially looking for row to fill in 
        for k in range(n):
            j = k + 1
            while row[k] > k and j < n:
                if row[j] <= k:
                    for i in range(j, k, -1):
                        row[i-1], row[i] = row[i], row[i-1]
                        ans += 1
                else:
                    j += 1
            if row[k] > k:
                return -1
        return ans 
# @lc code=end

