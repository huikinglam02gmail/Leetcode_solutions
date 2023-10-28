#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
class Solution:
    '''
    Clearly, a state machine problem
    Should be possible to solve by matrix multiplication!
    dp[n][k]: number of strings of length n that can be formed with end "k"
    k = 0: "a"; k = 1: "e"; k = 2: "i"; k = 3: "o"; k = 4: "u"
    Then construct the transition matrix T:
     [[0,1,1,0,1], 
      [1,0,1,0,0],
      [0,1,0,1,0],
      [0,0,1,0,0],
      [0,0,1,1,0]]
    Then for n, break it down into bit representation
    keep calculating and multiplying two powers of T   
    '''

    def matrix_multiply(self, M1, M2):
        m1, n1, n2 = len(M1), len(M1[0]), len(M2[0])
        res = [[0 for i in range(n2)] for j in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(n1):
                    res[i][j] += M1[i][k]*M2[k][j]
                    res[i][j] %= self.MOD
        return res
    
    def countVowelPermutation(self, n: int) -> int:
        self.MOD = pow(10,9) + 7
        seed = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            seed[i][i] = 1
        T = [[0,1,1,0,1],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,1,0]]
        bl = n.bit_length()
        for i in range(bl):
            if (n - 1) & (1 << i) != 0:
                seed = self.matrix_multiply(T, seed)
            T = self.matrix_multiply(T,T)
        result = 0
        for i in range(5):
            for j in range(5):
                result += seed[i][j]
                result %= self.MOD
        return result
# @lc code=end

