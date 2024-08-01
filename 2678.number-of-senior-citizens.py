#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for detail in details: 
            if int(detail[11:13]) > 60: result += 1
        return result
# @lc code=end
