#
# @lc app=leetcode id=3121 lang=python3
#
# [3121] Count the Number of Special Characters II
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = {}
        for i in range(len(word)):
            if word[i] not in seen: seen[word[i]] = [i]
            else: seen[word[i]].append(i)

        result = 0
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c not in seen: continue
            if c.lower() not in seen: continue
            if seen[c][0] > seen[c.lower()][-1]: result += 1
        return result
# @lc code=end

