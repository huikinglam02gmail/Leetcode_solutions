#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash_chars = [0]*26
        for c in chars: hash_chars[ord(c) - ord('a')] += 1
        result = 0
        for word in words:
            hash_word = [0]*26
            for c in word: hash_word[ord(c) - ord('a')] += 1
            if all([a <= b for a, b in zip(hash_word, hash_chars)]): result += len(word)
        return result
# @lc code=end

