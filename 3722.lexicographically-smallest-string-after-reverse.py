#
# @lc app=leetcode id=3722 lang=python3
#
# [3722] Lexicographically Smallest String After Reverse
#

# @lc code=start
class Solution:
    def lexSmallest(self, s: str) -> str:
        result = s
        for i in range(len(s)):
            reversed_s = s[:i] + s[i:][::-1]
            if reversed_s < result: result = reversed_s
        for i in range(len(s)):
            reversed_s = s[:i][::-1] + s[i:]
            if reversed_s < result: result = reversed_s
        return result
# @lc code=end

