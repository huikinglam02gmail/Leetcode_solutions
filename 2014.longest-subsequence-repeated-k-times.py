#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    If we divide s into k segments, the length of longest subsequence cannot exceed n // k, because it would mean it uses every character in each segment.
    In here we have 2 <= n < k * 8, so n // k < 8, therefore we know our answer can only be length 7 or shorter
    Then the next task is to record occurrence of all characters. A character c can appear <= occur[c] // k times.
    Thirdly, we assemble all candidates of subsequences: Go down from long (length = n // k) to short (length = 1) and lexicographically large to small
    '''
    '''
    Check if s is a subsequence of t
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)

    '''
    Given remaining available characters and number of remaining characters in possible subsequences, generate all possible subsequences
    '''
    @lru_cache(None)
    def generateCandidates(self, remainCharacters, availableCharacters):
        result = set([""]) if remainCharacters == 0 else set()
        if remainCharacters > 0:
            for i, c in enumerate(availableCharacters):
                if i > 0 and c == availableCharacters[i - 1]: continue
                furtherSearchSet = self.generateCandidates(remainCharacters - 1, availableCharacters[:i] + availableCharacters[i+1:])
                for s in furtherSearchSet: result.add(c + s)
        return result


    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        occur = [0] * 26
        n = len(s)
        for c in s: occur[ord(c) - ord('a')] += 1
        startingString = ""
        for i in range(25, -1, -1):
            startingString += chr(i + ord('a')) * (occur[i] // k)

        for i in range(min(n // k, len(startingString)), 0, -1):
            candidates = sorted(self.generateCandidates(i, startingString), reverse=True)
            for cand in candidates:
                if self.isSubsequence(cand * k, s):
                    return cand
        return ""
        
# @lc code=end

