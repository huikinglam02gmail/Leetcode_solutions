#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Initiate two result arrays results[i] starts with elements with groups[i] 
    For each word, if group[i] == j, append to results[1 - j] if len(results[1 - j]) is odd, append to results[j] is len(results[j]) is even 
    return the longer one
    '''
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        results = [[] for i in range(2)]
        for word, group in zip(words, groups):
            if not len(results[group]) % 2: results[group].append(word)
            if len(results[1 - group]) % 2: results[1 - group].append(word)
        return results[0] if len(results[0]) >= len(results[1]) else results[1]
# @lc code=end

