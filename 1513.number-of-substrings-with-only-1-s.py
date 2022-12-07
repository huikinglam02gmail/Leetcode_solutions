#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#

# @lc code=start
class Solution:
    # No need for sliding window
    # a consecutive streak of n 1s will have n '1', n-1 '11',..., 1 '1'*n
    # Contribution will be 1 + 2 + ... + n = n(n+1)/2
    def numSub(self, s: str) -> int:
        consec, result, MOD = 0, 0, pow(10,9) + 7
        for c in s:
            if c == '1':
                consec += 1
            elif consec > 0:
                result += consec*(consec + 1) // 2
                result %= MOD
                consec = 0
        result += consec*(consec + 1) // 2
        result %= MOD
        return result
# @lc code=end

