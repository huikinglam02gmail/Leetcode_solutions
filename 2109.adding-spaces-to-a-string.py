#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        dq = deque()
        ns, nSpace, j = len(s), len(spaces), 0
        for i in range(ns):
            if j < nSpace and i == spaces[j]:
                dq.append(" ")
                j += 1
            dq.append(s[i])
        result = ""
        while dq: result += dq.popleft()
        return result
# @lc code=end

