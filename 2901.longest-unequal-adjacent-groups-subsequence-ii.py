#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#

# @lc code=start
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        wordLengths = {}
        dp = []
        prev = [-1] * len(words)
        for i, word in enumerate(words):
            current = 1
            if len(word) in wordLengths:
                for j in wordLengths[len(word)]:
                    if groups[i] != groups[j] and self.Hamming(words[j], word) == 1 and current < dp[j] + 1:
                        current = max(current, 1 + dp[j])
                        prev[i] = j
            if len(word) not in wordLengths: wordLengths[len(word)] = []
            wordLengths[len(word)].append(i)
            dp.append(current)
        maxIndex = dp.index(max(dp))
        result = []
        while maxIndex != -1:
            result.append(words[maxIndex])
            maxIndex = prev[maxIndex]
        return result[::-1]       
    
    def Hamming(self, word1: str, word2: str) -> int:
        return sum([1 for i in range(len(word1)) if word1[i] != word2[i]])
# @lc code=end

