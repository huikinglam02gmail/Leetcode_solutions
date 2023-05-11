#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        limit = [0, len(matrix), 0, len(matrix[0])]
        total = len(matrix) * len(matrix[0])
        counter = 0
        while (limit[0] < limit[1] or limit[2] < limit[3]) and counter < len(matrix)*len(matrix[0]):
            current_row = limit[0]
            for i in range(limit[2], limit[3]):
                result.append(matrix[current_row][i])
                counter += 1
                if counter == total: return result
            limit[0] += 1
            current_column = limit[3] - 1
            for i in range(limit[0], limit[1]):
                result.append(matrix[i][current_column])
                counter += 1
                if counter == total: return result
            limit[3] -= 1
            current_row = limit[1] - 1
            for i in range(limit[3] - 1,limit[2] - 1, -1):
                result.append(matrix[current_row][i])
                counter += 1
                if counter == total: return result
            limit[1] -= 1
            current_column = limit[2]
            for i in range(limit[1] - 1,limit[0] - 1, -1):
                result.append(matrix[i][current_column])
                counter += 1
                if counter == total: return result
            limit[2] += 1
# @lc code=end

