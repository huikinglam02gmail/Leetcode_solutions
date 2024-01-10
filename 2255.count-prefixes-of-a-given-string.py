#
# @lc app=leetcode id=2255 lang=python3
#
# [2255] Count Prefixes of a Given String
#

# @lc code=start
from typing import List


class Solution:
    '''
    use startWith
    '''
    def countPrefixes(self, words: List[str], s: str) -> int:
        result = 0
        for word in words:
            if s.startswith(word): result += 1
        return result
# @lc code=end

