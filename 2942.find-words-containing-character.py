#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        result = []
        for i in range(n):
            if x in words[i]: result.append(i)
        return result
# @lc code=end

