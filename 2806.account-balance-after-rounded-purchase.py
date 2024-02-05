#
# @lc app=leetcode id=2806 lang=python3
#
# [2806] Account Balance After Rounded Purchase
#

# @lc code=start
class Solution:
    def round(self, i):
        residual = i // 10
        if i % 10 < 5: return residual * 10
        else: return residual * 10 + 10
    
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - self.round(purchaseAmount)
# @lc code=end

