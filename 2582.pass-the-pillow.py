#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    '''
    simple math. one cycle take 2 * (n - 1)
    Take the modulo time % (2 * (n - 1)) = t. Then i will hold ball at times i - 1 and 2 * (n - 1) - (i - 1) = 2 * n - i - 1
    so if 1 <= t + 1 <= n, return t + 1
    else return 2 * n - 1 - t
    '''
    def passThePillow(self, n: int, time: int) -> int:
        t = time % (2 * (n - 1))
        if 0 <= t <= n - 1: return t + 1
        else: return 2 * n - 1 - t
# @lc code=end

