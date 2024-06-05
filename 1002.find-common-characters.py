#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = [0] * 26
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i, word in enumerate(words):
            for j in range(26):
                if i == 0: count[j] = word.count(alphabets[j])
                else: count[j] = min(count[j], word.count(alphabets[j]))
        result = []
        for i in range(26):
            if count[i] > 0: result += [chr(i + ord('a'))] * count[i]
        return result
                
# @lc code=end

