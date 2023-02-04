#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    # Draw the sequences out
    # Then construct the string
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        for i, c in enumerate(s):
            if (i % (2*(numRows-1)) < numRows - 1):
                rows[i % (2*(numRows-1))].append(s[i])
            else:
                rows[2*(numRows - 1) - i % (2*(numRows-1))].append(s[i])        
        result = ""
        for i in range(numRows):
            result += "".join(rows[i])
        return result
        
# @lc code=end

