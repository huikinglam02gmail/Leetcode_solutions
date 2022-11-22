#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    # The maximum answer must be either 1, 2, 3 or 4 (Lagrange's four-square theorem)
    # If n is a perfect square, return 1
    # If n is a sum of two perfect squares, return 2
    # Else, we use Legendre's three-square theorem and test if
    # n = 4^a*(8*b + 7)
    def numSquares(self, n: int) -> int:
        perfect = []
        for i in range(1,101,1):
            perfect.append(i*i)
            if i*i == n:
                return 1
        index = 0
        while n > perfect[index]:
            if n - perfect[index] in perfect:
                return 2
            index += 1
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        else: 
            return 3
# @lc code=end

