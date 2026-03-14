#
# @lc app=leetcode id=3838 lang=python3
#
# [3838] Weighted Word Mapping
#

# @lc code=start
from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            weight = sum(weights[ord(ch) - ord('a')] for ch in word)
            result += chr(ord('z') - (weight % 26))
        return result
# @lc code=end

