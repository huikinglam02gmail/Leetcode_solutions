#
# @lc app=leetcode id=2729 lang=python3
#
# [2729] Check if The Number is Fascinating
#

# @lc code=start
class Solution:
    def isFascinating(self, n: int) -> bool:
        resultString = ""
        for i in range(1, 4, 1):
            resultString += str(i * n)
        for i in range(1, 10, 1):
            if resultString.count(str(i)) != 1:
                return False
        return True
        
# @lc code=end

