#
# @lc app=leetcode id=1754 lang=python3
#
# [1754] Largest Merge Of Two Strings
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    1 <= word1.length, word2.length <= 3000
    We can easily compare between remaining substrings of word1 and word2. If word1 >= word2, that means we should get word1[0]. Otherwise, we should get word2[0], because during the comparison of remaining characters, we already find which one we should pick. 
    '''

    def largestMerge(self, word1: str, word2: str) -> str:
        i, j, n1, n2 = 0, 0, len(word1), len(word2)

        @lru_cache(None)
        def dfs(i, j):
            if i == n1:
                return word2[j:]
            elif j == n2:
                return word1[i:]
            elif word1[i:] >= word2[j:]:
                return word1[i] + dfs(i + 1, j)
            else:
                return word2[j] + dfs(i, j + 1)
        
        return dfs(0,0)
# @lc code=end
