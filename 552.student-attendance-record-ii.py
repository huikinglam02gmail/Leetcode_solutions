#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def matrix_multiply(self, A, B, MOD):
        n = len(A)
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    C[i][k] += A[i][j]*B[j][k] % MOD
        return C
    
    '''
    6 possible states:
     a. no A, end with no L
     b. no A, end with 1 L
     c. no A, end with 2 L
     d. 1 A, end with no L
     e. 1 A, end with 1 L
     f. 1 A, end with 2 L
    After a round, the number possible changes as follow:
    b' = a, c' = b, e' = d, f' = e, a' = (a+b+c), d' = (a+b+c+d+e+f)
    Therefore we can DP solution up from n = 1
    O(N) time
    Alternatively one should note that this is a matrix multiplication problem:
    v = A^(n+1) u
    Then split (n+1) into binary representation
    A^(n+1) = A^(k_i*2^i + ....)        
    '''
    def checkRecord(self, n: int) -> int:
        MOD = pow(10,9)+7
        A = [[1,1,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,1,1,1,1,1],[0,0,0,1,0,0],[0,0,0,0,1,0]]
        # number of bits needed to represent n+1
        temp = n
        count = 0
        while temp > 0:
            count += 1
            temp //= 2
        B = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        for i in range(count):
            if n & (1 << i): B = self.matrix_multiply(A,B,MOD)
            A = self.matrix_multiply(A,A,MOD)
        result = 0
        u = [1,1,0,1,0,0]
        for i in range(6):
            result += B[3][i]*u[i]
        return result % MOD
# @lc code=end

