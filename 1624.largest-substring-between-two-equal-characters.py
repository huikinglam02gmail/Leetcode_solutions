#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        occur = [[] for i in range(26)]
        for i, c in enumerate(s): occur[ord(c) - ord('a')].append(i)
        result = - 1
        for i in range(26):
            if occur[i]: result = max(result, occur[i][-1] - occur[i][0] - 1)
        return result
# @lc code=end

