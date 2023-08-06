#
# @lc app=leetcode id=1839 lang=python3
#
# [1839] Longest Substring Of All Vowels in Order
#

# @lc code=start
from collections import deque


class Solution:
    '''
    This is a sliding window problem.
    Pretty much we can add to the current string the current character
    Since we only have aeiou, we just need to find if the appearance of a, e, i, o and u are sorted.
    If not, any further indices would not be beautiful.
    For example if word = "aeiaaioaaaaeiiiiouuuooaauuaeiu" When we have current valid string to be "aei", and when "a" comes in, we check if "e", "i", "o" and "u" has occurred. If so, pop them.
    '''
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        indices = [deque() for i in range(5)] 
        result = 0
        for ind, c in enumerate(word):
            for i in range(vowels[c] + 1, 5, 1):
                while len(indices[i]) > 0:
                    for j in range(0, i, 1):
                        while indices[j] and indices[j][0] < indices[i][0]:
                            indices[j].popleft()
                    indices[i].popleft()
            indices[vowels[c]].append(ind)
            if all([len(x) > 0 for x in indices]):
                result = max(result, sum([len(x) for x in indices]))
        return result
        
# @lc code=end

