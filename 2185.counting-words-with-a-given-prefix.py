#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if word[0:len(pref)] == pref: result += 1
        return result
        
# @lc code=end

