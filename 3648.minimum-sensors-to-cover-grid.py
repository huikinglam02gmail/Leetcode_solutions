#
# @lc app=leetcode id=3648 lang=python3
#
# [3648] Minimum Sensors to Cover Grid
#

# @lc code=start
class Solution:
    '''
    ceil division
    '''
    def ceildiv(self, a, b):
        return -(a // -b)


    def minSensors(self, n: int, m: int, k: int) -> int:
        return self.ceildiv(n, 2 * k + 1) * self.ceildiv(m, 2 * k + 1)
# @lc code=end

