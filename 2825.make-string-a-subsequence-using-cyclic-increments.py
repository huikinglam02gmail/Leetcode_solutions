#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
class Solution:
    '''
    variant of the isSubsequence problem
    '''
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for c in str1:
            if i < len(str2) and (str2[i] == c or (ord(str2[i]) - ord(c) + 26)  % 26 == 1): i += 1
        return i == len(str2)
        
# @lc code=end

