#
# @lc app=leetcode id=2135 lang=python3
#
# [2135] Count Words Obtained After Adding a Letter
#

# @lc code=start
from typing import List


class Solution:
    '''
    use bitmask to represent each word, as each word has no repetitive characters
    For each word in targetWords, ask if removing one character in its bitmask will is present in startWords
    '''
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords:
            mask = 0
            for c in word: mask ^= (1 << (ord(c) - ord('a')))
            seen.add(mask)
        result = 0
        for word in targetWords:
            mask = 0
            for c in word: mask ^= (1 << (ord(c) - ord('a')))
            for c in word:
                mask ^= (1 << (ord(c) - ord('a')))
                if mask in seen:
                    result += 1
                    break
                else:
                    mask ^= (1 << (ord(c) - ord('a')))
        return result           
        # @lc code=end

