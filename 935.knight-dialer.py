#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
class Solution:
    '''
    This look like a matrix multiplication problem
    At least, we see that there are well defined transitions possible
    1 -> 6, 8
    2 -> 7, 9
    3 -> 4, 8
    4 -> 3, 9, 0
    5 -> {}
    6 -> 1, 7, 0
    7 -> 2, 6
    8 -> 1, 3
    9 -> 2, 4
    0 -> 4, 6
    The transition matrix M is well defined
    Then we can break down n into power of 2s. (n >> i = 1 or not)
    And just sum up the matrix contribution each time it is squared    
    '''

    def matrix_multiply(self, A, C):
        n = len(A)
        B = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    B[i][j] += A[i][k]*C[k][j] 
                    B[i][j] %= self.MOD
        return B
    
    def knightDialer(self, n: int) -> int:
        self.MOD = pow(10, 9) + 7
        M = [[0,0,0,0,1,0,1,0,0,0],
             [0,0,0,0,0,0,1,0,1,0],
             [0,0,0,0,0,0,0,1,0,1],
             [0,0,0,0,1,0,0,0,1,0],
             [1,0,0,1,0,0,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,1,0,0],
             [0,0,1,0,0,0,1,0,0,0],
             [0,1,0,1,0,0,0,0,0,0],
             [0,0,1,0,1,0,0,0,0,0]]
        seed = [[1 if i == j else 0 for i in range(10)] for j in range(10)]      
        
        for i in range((n-1).bit_length()):
            if (n - 1) & (1 << i) != 0:
                seed = self.matrix_multiply(seed, M)
            M = self.matrix_multiply(M, M)
        
        result = 0    
        for j in range(10):
            for k in range(10):
                result += seed[j][k]
                result %= self.MOD
        return result
# @lc code=end

