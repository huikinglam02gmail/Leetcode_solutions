#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

# @lc code=start
class Solution:
    '''
    Can only form substrings with all same characters within chunks. Will length l, number of substring = 1 + 2 + ... + l = l*(l + 1) // 2
    '''
    def countHomogenous(self, s: str) -> int:
        MOD = pow(10,9) + 7
        n = len(s)
        l = 0
        result = 0
        while l < n:
            r = l + 1
            while r < n and s[l] == s[r]:
                r += 1
            result += (r - l ) * (r - l + 1) // 2
            result %= MOD
            l = r
        return result

        
# @lc code=end

