#
# @lc app=leetcode id=3898 lang=python3
#
# [3898] Find the Degree of Each Vertex
#

# @lc code=start
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]
# @lc code=end

