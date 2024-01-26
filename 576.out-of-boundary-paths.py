#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
class Solution:
    '''
    DP problem
    Count number of times the ball can arrive at the edge for each number of moves    
    '''
    def scores(self, row, col, m, n):
        count = 0
        if row == 0:
            count += 1
        if col == 0:
            count += 1
        if row == m - 1:
            count += 1
        if col == n - 1:
            count += 1
        return count
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        MOD = pow(10,9) + 7
        # Get the coordinates of hash map of corners and edges to store the number of exit ways 
        hash_table =  {}
        for i in range(m):
            for j in range(n):
                score = self.scores(i, j, m, n)
                if score > 0:
                    hash_table[(i,j)] = score
        result = 0
        # Keep counting numbers of balls possible in each position
        # Count the edge and corners scores * the dp count
        for move in range(maxMove):
            if move == 0:
                dp[startRow][startColumn] = 1
                if (startRow, startColumn) in hash_table:
                    result += hash_table[(startRow, startColumn)]
                    result %= MOD
            else:
                dp_new = [[0 for i in range(n)] for j in range(m)]
                for i in range(m):
                    for j in range(n):
                        if i >= 1:
                            dp_new[i][j] += dp[i - 1][j]
                        if j >= 1:
                            dp_new[i][j] += dp[i][j - 1]
                        if i < m - 1:
                            dp_new[i][j] += dp[i + 1][j]
                        if j < n - 1:
                            dp_new[i][j] += dp[i][j + 1]
                        if (i,j) in hash_table:
                            result += dp_new[i][j] * hash_table[(i,j)]
                            result %= MOD
                dp = dp_new[:]
        return result
# @lc code=end

