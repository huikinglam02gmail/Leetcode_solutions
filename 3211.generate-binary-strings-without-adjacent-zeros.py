#
# @lc app=leetcode id=3211 lang=python3
#
# [3211] Generate Binary Strings Without Adjacent Zeros
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP problem.
    Just expand from n = 1
    '''
    def validStrings(self, n: int) -> List[str]:
        dp = ["0", "1"]
        for i in range(n - 1):
            dpNew = []
            for s in dp:
                if s[-1] == "1": dpNew.append(s + "0")
                dpNew.append(s + "1")
            dp = dpNew[:]
        return dp
# @lc code=end

