#
# @lc app=leetcode id=3014 lang=python3
#
# [3014] Minimum Number of Pushes to Type Word I
#

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        n = len(word)
        for i in range(n): result += 1 + (i // 8)
        return result
# @lc code=end

