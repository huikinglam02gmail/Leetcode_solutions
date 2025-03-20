#
# @lc app=leetcode id=3039 lang=python3
#
# [3039] Apply Operations to Make String Empty
#

# @lc code=start
from collections import deque


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        occur = [[] for i in range(26)]
        for i, c in enumerate(s): occur[ord(c) - ord('a')].append(i)
        maxLength = 0
        for i in range(26): maxLength = max(maxLength, len(occur[i]))
        finalArray = []
        for i in range(26):
            if len(occur[i]) == maxLength: finalArray.append([occur[i][-1], i])
        finalArray.sort()
        result = ""
        for i, c in finalArray: result += chr(c + ord('a'))
        return result

# @lc code=end

