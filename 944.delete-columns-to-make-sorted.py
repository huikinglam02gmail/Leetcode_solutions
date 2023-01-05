#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n, result = len(strs), len(strs[0]), 0
        for i in range(n):
            for j in range(m -1):
                if ord(strs[j+1][i]) < ord(strs[j][i]):
                    result += 1
                    break
        return result
# @lc code=end

