#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# @lc code=start
class Solution:
    # DP problem
    # dp(i,j,c) = Return the number of ways of cutting pizza[i:][j:]
    # such that each piece contains at least one apple and there are c cuts left
    # In order to make sure the pieces after cut has at least one apple
    # We reuse code from 304. Range Sum Query 2D - Immutable
    def ways(self, pizza: List[str], k: int) -> int:
        
# @lc code=end

