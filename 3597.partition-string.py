#
# @lc app=leetcode id=3597 lang=python3
#
# [3597] Partition String 
#

# @lc code=start
from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = {}
        index = 0
        current = ""
        for c in s:
            current += c
            if current not in seen:
                seen[current] = index
                index += 1
                current = ""
        result = [""] * index
        for seenString in seen:
            result[seen[seenString]] = seenString
        return result
# @lc code=end

