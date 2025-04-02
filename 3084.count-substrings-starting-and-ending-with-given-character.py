#
# @lc app=leetcode id=3084 lang=python3
#
# [3084] Count Substrings Starting and Ending with Given Character
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return count * (count + 1) // 2
# @lc code=end

