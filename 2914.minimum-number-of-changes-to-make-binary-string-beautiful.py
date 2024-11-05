#
# @lc app=leetcode id=2914 lang=python3
#
# [2914] Minimum Number of Changes to Make Binary String Beautiful
#

# @lc code=start
class Solution:
    '''
    A long block of even length substring always require more changes to maintain than shorter ones. We should consider consecutive length two substrings.
    '''
    def minChanges(self, s: str) -> int:
        result = 0
        for i in range(len(s) // 2):
            if s[2 * i] != s[2 * i + 1]: result += 1
        return result
# @lc code=end

