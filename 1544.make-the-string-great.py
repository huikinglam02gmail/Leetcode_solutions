#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if result and abs(ord(c) - ord(result[-1])) == 32:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
# @lc code=end

