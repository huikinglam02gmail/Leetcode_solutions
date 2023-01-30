#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
            t3 = t0 + t1 + t2
            for i in range(3,n):
                t3, t2, t1, t0 = t3 + t2 + t1, t3, t2, t1
            return t3
            # @lc code=end

