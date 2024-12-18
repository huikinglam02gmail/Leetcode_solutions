#
# @lc app=leetcode id=3222 lang=python3
#
# [3222] Find the Winning Player in Coin Game
#

# @lc code=start
class Solution:
    def win(self, x, y, turn):
        if x < 1 or y < 4: return turn
        else: return self.win(x - 1, y - 4, 1 - turn)

    def winningPlayer(self, x: int, y: int) -> str:
        if self.win(x, y, 0) == 0: return "Bob"
        else: return "Alice"

# @lc code=end

