#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        cur, result = "", 0
        for c in s:
            if c in cur:
                result += 1
                cur = ""
            cur += c
        return result + 1
# @lc code=end

