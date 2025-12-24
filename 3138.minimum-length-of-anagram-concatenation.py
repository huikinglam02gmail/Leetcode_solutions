#
# @lc app=leetcode id=3138 lang=python3
#
# [3138] Minimum Length of Anagram Concatenation
#

# @lc code=start
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for i in range(1, n + 1, 1):
            if n % i == 0:
                if self.isAnagram(s, i): return i
            i += 1
        return -1

    def isAnagram(self, s: str, l: int) -> bool:
        count = [0] * 26
        for i in range(0, len(s), l):
            countNew = [0] * 26
            for j in range(i, i + l):
                countNew[ord(s[j]) - ord("a")] += 1
            if i > 0:
                for j in range(26):
                    if count[j] != countNew[j]: return False
            count = countNew.copy()
        return True
# @lc code=end

