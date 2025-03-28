#
# @lc app=leetcode id=2767 lang=python3
#
# [2767] Partition String Into Minimum Beautiful Substrings
#

# @lc code=start
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        self.fiveSet = []
        i = 1
        while len(str(bin(i)[2:])) <= 15:
            self.fiveSet.append(str(bin(i)[2:]))
            i *= 5
        result = self.backtrack(s)
        return result if result != float("inf") else -1

    def backtrack(self, s):
        if s in self.fiveSet: return 1
        result = float("inf")
        for five in self.fiveSet:
            if s.startswith(five): result = min(result, 1 + self.backtrack(s[len(five):]))
        return result
        
# @lc code=end

