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
        result = ""
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and spaces[j] == i: 
                result += " "
                j += 1            
            result += s[i]
        return result

# @lc code=end

