#
# @lc app=leetcode id=2939 lang=python3
#
# [2939] Maximum Xor Product
#

# @lc code=start
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = pow(10, 9) + 7
        for i in range(n - 1, -1, -1):
            if ((min(a, b) & (1 << i)) == 0):
                a ^= (1 << i)
                b ^= (1 << i)
        return ((a % MOD) * (b % MOD)) % MOD
# @lc code=end
