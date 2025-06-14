#
# @lc app=leetcode id=3560 lang=python3
#
# [3560] Find Minimum Log Transportation Cost
#

# @lc code=start
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        na = n // k
        if n % k == 0: na -= 1
        ma = m // k
        if m % k == 0: ma -= 1
        res = 0
        if na: res += k * (n - (na * (na + 1) // 2) * k)
        if ma: res += k * (m - (ma * (ma + 1) // 2) * k)
        return res
# @lc code=end

