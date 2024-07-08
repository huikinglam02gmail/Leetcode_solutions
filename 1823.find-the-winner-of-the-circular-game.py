#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    '''
    Josephus problem
    The problem has a recursive nature that would allow for dynamic programming
    When 1 person is killed, the people size becomes n - 1, and the labelling starts at k    
    '''
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return 1
        else: return (self.findTheWinner(n - 1, k ) + k - 1) % n + 1
# @lc code=end

