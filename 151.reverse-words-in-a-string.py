#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split(' ')
        result, n = [], len(sSplit)
        for i in range(n-1,-1,-1):
            if sSplit[i] != '':
                result.append(sSplit[i])
        return ' '.join(result)
# @lc code=end

