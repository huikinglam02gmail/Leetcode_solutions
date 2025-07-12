#
# @lc app=leetcode id=3044 lang=python3
#
# [3044] Most Frequent Prime
#

# @lc code=start
import math
from typing import List


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        primeCount = {}
        increments = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1],[-1, 1], [-1, -1]]
        for i in range(m):
            for j in range(n):
                for incX, incY in increments:
                    i1, j1 = i, j
                    current = ""
                    while 0 <= i1 < m and 0 <= j1 < n:
                        current += str(mat[i1][j1])
                        i1 += incX
                        j1 += incY
                    for k in range(2, len(current) + 1):
                        if self.isPrime(int(current[:k])):
                            primeCount[int(current[:k])] = primeCount.get(int(current[:k]), 0) + 1
        if len(primeCount) == 0: return -1
        data = sorted(primeCount.items(), key=lambda x: (-x[1], - x[0]))
        return data[0][0]

    '''
    Function that returns True if n is prime else returns False    
    ''' 
    def isPrime(self, n):        
        if(n <= 1): return False
        if(n <= 3): return True
        
        if(n % 2 == 0 or n % 3 == 0): return False
        
        for i in range(5,int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0): return False       
        return True
# @lc code=end

