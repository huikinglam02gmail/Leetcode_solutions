#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
from typing import List


class Solution:
    '''
    We first store the row and column of each server
    Assign server IDs to each server
    Then we go through the server list
    For each server, we check their column and row in the hash table
    if either of the lengths is longer than 1, it means it is connected    
    '''
    def countServers(self, grid: List[List[int]]) -> int:
        servers, m, n = [], len(grid), len(grid[0])
        rows, cols, result = [0]*m, [0]*n, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    servers.append([i,j])
                    rows[i] += 1
                    cols[j] += 1
        
        for x, y in servers:
            if rows[x] > 1 or cols[y] > 1: result += 1
        return result
# @lc code=end

