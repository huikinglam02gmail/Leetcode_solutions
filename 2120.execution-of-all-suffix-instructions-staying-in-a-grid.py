#
# @lc app=leetcode id=2120 lang=python3
#
# [2120] Execution of All Suffix Instructions Staying in a Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just simulate the process
    '''
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            x, y = startPos
            wordPos = i
            while 0 <= x < n and 0 <= y < n and wordPos < len(s):
                if s[wordPos] == "R": y += 1
                elif s[wordPos] == "L": y -= 1
                elif s[wordPos] == "U": x -= 1
                else: x += 1
                wordPos += 1
            result.append(wordPos - i - (x < 0 or x == n or y < 0 or y == n))
        return result
# @lc code=end

