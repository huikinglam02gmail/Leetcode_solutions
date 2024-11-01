#
# @lc app=leetcode id=3248 lang=python3
#
# [3248] Snake in Matrix
#

# @lc code=start
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0
        for command in commands:
            if command == "UP": pos -= n
            elif command == "RIGHT": pos += 1
            elif command == "LEFT": pos -= 1
            else: pos += n
        return pos
# @lc code=end

