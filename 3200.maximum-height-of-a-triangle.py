#
# @lc app=leetcode id=3200 lang=python3
#
# [3200] Maximum Height of a Triangle
#

# @lc code=start
class Solution:
    def build(self, lastRow, lastColor, red, blue):
        result = 0
        if lastColor == 0 and blue >= lastRow + 1: result = 1 + self.build(lastRow + 1, 1 - lastColor, red, blue - lastRow - 1)
        elif lastColor == 1 and red >= lastRow + 1: result = 1 + self.build(lastRow + 1, 1 - lastColor, red - lastRow - 1, blue)
        return result

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.build(0, 0, red, blue), self.build(0, 1, red, blue))
        
# @lc code=end

