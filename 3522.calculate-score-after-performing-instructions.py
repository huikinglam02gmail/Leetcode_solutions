#
# @lc app=leetcode id=3522 lang=python3
#
# [3522] Calculate Score After Performing Instructions
#

# @lc code=start
from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = [False] * n
        result = 0
        pos = 0
        while 0 <= pos < n and not visited[pos]:
            visited[pos] = True
            if instructions[pos] == "add":
                result += values[pos]
                pos += 1
            else:
                pos += values[pos]
        return result
# @lc code=end

