#
# @lc app=leetcode id=3271 lang=python3
#
# [3271] Hash Divided String
#

# @lc code=start
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        for j in range(len(s) // k):
            total = 0
            for c in s[k * j : k * j + k]: total += ord(c) - ord('a')
            result.append(chr(ord('a') + total % 26))
        return "".join(result)

# @lc code=end

