#
# @lc app=leetcode id=2930 lang=python3
#
# [2930] Number of Strings Which Can Be Rearranged to Contain Substring
#

# @lc code=start
class Solution:
    def matrix_multiply(self, A, B, MOD):
        m = len(A)
        n = len(B[0])
        C = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for k in range(n):
                for j in range(len(B)):
                    C[i][k] += A[i][j]*B[j][k]
                    C[i][k] %= MOD
        return C
    '''
    dp[i][0] = number of strings of length i + 1 that contains ""
    dp[i][1] = number of strings of length i + 1 that contains "l"
    dp[i][2] = number of strings of length i + 1 that contains "e"
    dp[i][3] = number of strings of length i + 1 that contains "t"
    dp[i][4] = number of strings of length i + 1 that contains "le"
    dp[i][5] = number of strings of length i + 1 that contains "et"
    dp[i][6] = number of strings of length i + 1 that contains "lt"
    dp[i][7] = number of strings of length i + 1 that contains "ee"
    dp[i][8] = number of strings of length i + 1 that contains "lee"
    dp[i][9] = number of strings of length i + 1 that contains "let"
    dp[i][10] = number of strings of length i + 1 that contains "eet"
    dp[i][11] = number of strings of length i + 1 that contains "leet"
    We have this recurrence relation:
    dp[i + 1][0] = 23 * dp[i][0]
    dp[i + 1][1] = 24 * dp[i][1] + dp[i][0]
    dp[i + 1][2] = 23 * dp[i][2] + dp[i][0]
    dp[i + 1][3] = 24 * dp[i][3] + dp[i][0]
    dp[i + 1][4] = 24 * dp[i][4] + dp[i][1] + dp[i][2]
    dp[i + 1][5] = 24 * dp[i][5] + dp[i][2] + dp[i][3]
    dp[i + 1][6] = 25 * dp[i][6] + dp[i][1] + dp[i][3]
    dp[i + 1][7] = 24 * dp[i][7] + dp[i][2]
    dp[i + 1][8] = 25 * dp[i][8] + dp[i][4] + dp[i][7]
    dp[i + 1][9] = 25 * dp[i][9] + dp[i][4] + dp[i][5] + dp[i][6]
    dp[i + 1][10] = 25 * dp[i][10] + dp[i][5] + dp[i][7]
    dp[i + 1][11] = 26 * dp[i][11] + dp[i][8] + dp[i][9] + dp[i][10]
    '''
    def stringCount(self, n: int) -> int:
        MOD = pow(10,9) + 7
        A = [[23,0,0,0,0,0,0,0,0,0,0,0],
             [1,24,0,0,0,0,0,0,0,0,0,0],
             [1,0,23,0,0,0,0,0,0,0,0,0],
             [1,0,0,24,0,0,0,0,0,0,0,0],
             [0,1,1,0,24,0,0,0,0,0,0,0],
             [0,0,1,1,0,24,0,0,0,0,0,0],
             [0,1,0,1,0,0,25,0,0,0,0,0],
             [0,0,1,0,0,0,0,24,0,0,0,0],
             [0,0,0,0,1,0,0,1,25,0,0,0],
             [0,0,0,0,1,1,1,0,0,25,0,0],
             [0,0,0,0,0,1,0,1,0,0,25,0],
             [0,0,0,0,0,0,0,0,1,1,1,26]]
        temp = n
        count = 0
        while temp > 0:
            count += 1
            temp //= 2
        B = [[1,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0],
             [0,0,0,0,0,0,0,0,0,0,0,1]]
        for i in range(count):
            if n & (1 << i): B = self.matrix_multiply(A,B,MOD)
            A = self.matrix_multiply(A,A,MOD)
        u = [[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
        C = self.matrix_multiply(B, u, MOD)
        return C[-1][0]
    # @lc code=end

