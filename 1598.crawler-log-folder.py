#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log[0:2] == '..':
                if result != 0:
                    result -= 1
            else:
                if log[0:2] != './':
                    result += 1
        return result
# @lc code=end

