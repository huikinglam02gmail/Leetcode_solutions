#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
      n = len(columnTitle)
      value = 0
      for i in range(n):
        c = columnTitle[i]
        value += (ord(c)-ord("A") + 1)*pow(26, n-1-i)
      return value
        
# @lc code=end

