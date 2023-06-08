#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution:
    '''
    Remove characters from two ends by two pointer
    '''
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        while i < j and s[i] == s[j]:
            common = s[i]
            while i < n and s[i] == common and i <= j:
                i += 1
            while j >= 0 and s[j] == common and i <= j:
                j -= 1
        if i == j:
            return 1
        else:
            return j - i + 1
# @lc code=end

