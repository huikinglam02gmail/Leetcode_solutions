#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        index = 0
        result = []
        while index + k <= len(s):
            result.append(s[index:index+k])
            index += k
        last_word = ''
        to_fill = k
        while index < len(s):
            last_word = last_word + s[index]
            to_fill -= 1
            index += 1
        if to_fill < k:
            for i in range(to_fill): last_word += fill
            result.append(last_word)
        return result
# @lc code=end

