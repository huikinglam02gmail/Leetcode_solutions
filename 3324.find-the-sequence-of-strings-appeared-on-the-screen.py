#
# @lc app=leetcode id=3324 lang=python3
#
# [3324] Find the Sequence of Strings Appeared on the Screen
#

# @lc code=start
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = ['a']
        while result[-1] != target:
            if result[-1][-1] < target[len(result[-1]) - 1]: result.append(result[-1][:-1:] + chr(ord(result[-1][-1]) + 1))
            else: result.append(result[-1] + "a")
        return result
# @lc code=end

