#
# @lc app=leetcode id=3274 lang=python3
#
# [3274] Check if Two Chessboard Squares Have the Same Color
#

# @lc code=start
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (ord(coordinate1[0]) - ord('a') + int(coordinate1[1])) % 2 == (ord(coordinate2[0]) - ord('a') + int(coordinate2[1])) % 2
# @lc code=end

