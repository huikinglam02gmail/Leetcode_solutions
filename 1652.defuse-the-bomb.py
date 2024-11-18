#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k != 0:
            step = 1 if k > 0 else -1
            for i in range(len(code)):
                for j in range(step, k + step, step):
                    result[i] += code[(i + j + len(code)) % len(code)] 
        return result
# @lc code=end

