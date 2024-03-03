#
# @lc app=leetcode id=3042 lang=python3
#
# [3042] Count Prefix and Suffix Pairs I
#

# @lc code=start
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n, 1):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1
        return result
# @lc code=end

