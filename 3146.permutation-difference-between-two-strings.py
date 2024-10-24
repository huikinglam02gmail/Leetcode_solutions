#
# @lc app=leetcode id=3146 lang=python3
#
# [3146] Permutation Difference between Two Strings
#

# @lc code=start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        sIndex, tIndex = [-1] * 26, [-1]*26
        for i in range(len(s)):
            sIndex[ord(s[i]) - ord('a')] = i
            tIndex[ord(t[i]) - ord('a')] = i
        for i in range(26): result += abs(sIndex[i] - tIndex[i])
        return result
# @lc code=end

