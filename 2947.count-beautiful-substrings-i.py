#
# @lc app=leetcode id=2947 lang=python3
#
# [2947] Count Beautiful Substrings I
#

# @lc code=start
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        vowels = set({'a','e','i','o','u'})
        ans = 0
        for i in range(N):
            c = v = 0
            for j in range(i, N):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                ans += c == v and not (v*c%k)
        return ans
        
# @lc code=end

