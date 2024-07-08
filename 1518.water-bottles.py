#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def helper(self, empty, full, numExchange):
        if full == 0: ans = 0
        else: ans = full + self.helper((full + empty) % numExchange, (full + empty) // numExchange, numExchange)
        return ans

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return self.helper(0, numBottles, numExchange)
# @lc code=end

