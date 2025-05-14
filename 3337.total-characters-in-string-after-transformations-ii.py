#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        M = [[0 for j in range(26)] for i in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1, 1):
                M[(i + j) % 26][i] += 1
        u = [[0] for i in range(26)]
        for c in s: u[ord(c) - ord('a')][0] += 1

        self.MOD = 1000000007
        seed = [[1 if i == j else 0 for i in range(26)] for j in range(26)]      
        
        while t > 0:
            if t & 1: seed = self.matrix_multiply(seed, M)
            M = self.matrix_multiply(M, M)
            t >>= 1
        
        result = 0
        v = self.matrix_multiply(seed, u)
        for i in range(26):
            result += v[i][0]
            result %= self.MOD
        return result
        

    def matrix_multiply(self, A, C):
        m, l = len(A), len(A[0])
        n = len(C[0])
        B = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(l):
                    B[i][j] += A[i][k] * C[k][j] 
                    B[i][j] %= self.MOD
        return B
# @lc code=end
