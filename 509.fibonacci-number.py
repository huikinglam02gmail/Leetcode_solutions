#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            old_1, old_2 = 0, 1
            new = old_1 + old_2
            for i in range(n-2):
                new, old_2, old_1 =  new + old_2, new, old_2
            return new
# @lc code=end

