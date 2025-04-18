#
# @lc app=leetcode id=3021 lang=python3
#
# [3021] Alice and Bob Playing Flower Game
#

# @lc code=start
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return self.ceildiv(n, 2) * (m // 2) + (n // 2) * self.ceildiv(m, 2)
    '''
    ceil division
    '''
    def ceildiv(self, a, b):
        return -(a // -b)
# @lc code=end

