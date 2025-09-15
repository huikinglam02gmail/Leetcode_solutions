#
# @lc app=leetcode id=3675 lang=python3
#
# [3675] Minimum Operations to Transform String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        result = 0
        for c in s:
            result = max(result, (ord('a') + 26 - ord(c)) % 26)
        return result
# @lc code=end

