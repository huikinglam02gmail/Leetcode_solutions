#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
from typing import List


class Solution:
    # Convert the alien word back to normal word
    # Then use string compare
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien = {}
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            alien[order[i]] = alphabets[i]
        
        alien_words = []
        for word in words:
            word_new = ""
            for c in word:
                word_new += alien[c]
            alien_words.append(word_new)
        
        
        for i in range(len(words)-1):
            if alien_words[i+1] < alien_words[i]:
                return False
        return True
        
# @lc code=end

