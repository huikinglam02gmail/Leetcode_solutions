#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        distinct = [0] * 10
        for i in digits: distinct[i] += 1
        result = []
        for i in range(100, 1000, 2):
            j = 0
            while j < 10:
                if str(i).count(str(j)) > distinct[j]: break
                j += 1
            if j == 10: result.append(i)
        return result

        
        
# @lc code=end

