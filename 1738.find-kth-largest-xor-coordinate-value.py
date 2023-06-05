#
# @lc app=leetcode id=1738 lang=python3
#
# [1738] Find Kth Largest XOR Coordinate Value
#

# @lc code=start
from typing import List


class Solution:
    '''
    We need to compute the prefix XOR array, then sort the array and get the number we want
    prefixXOR[i][j] = matrix[i][j]^prefixXOR[i-1][j]^prefixXOR[i][j - 1]^prefixXOR[i-1][j-1]
    '''
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefixXOR =[[matrix[i][j] for j in range(n)] for i in range(m)]
        allNumbers = []
        for i in range(m):
            for j in range(n):
                if i > 0:
                    prefixXOR[i][j] ^= prefixXOR[i - 1][j]
                if j > 0:
                    prefixXOR[i][j] ^= prefixXOR[i][j - 1]
                if i > 0 and j > 0:
                    prefixXOR[i][j] ^= prefixXOR[i - 1][j - 1]
                allNumbers.append(prefixXOR[i][j])
        allNumbers.sort(reverse=True)
        return allNumbers[k - 1]
        
# @lc code=end

