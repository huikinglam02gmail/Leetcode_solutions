#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sCount, tCount = [0] * 26, [0] * 26
        for S, T in zip(s, t):
            sCount[ord(S) - ord('a')] += 1
            tCount[ord(T) - ord('a')] += 1
        for i in range(26):
            if sCount[i] != tCount[i]: return False
        return True
            
# @lc code=end

