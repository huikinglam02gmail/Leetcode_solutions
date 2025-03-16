#
# @lc app=leetcode id=3483 lang=python3
#
# [3483] Unique 3-Digit Even Numbers
#

# @lc code=start
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()
        for i in range(len(digits) - 2):
            for j in range(i + 1, len(digits) - 1):
                for k in range(j + 1, len(digits)):
                    candidate = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
                    candidate = int(str(digits[i]) + str(digits[k]) + str(digits[j]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
                    candidate = int(str(digits[j]) + str(digits[i]) + str(digits[k]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
                    candidate = int(str(digits[j]) + str(digits[k]) + str(digits[i]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
                    candidate = int(str(digits[k]) + str(digits[i]) + str(digits[j]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
                    candidate = int(str(digits[k]) + str(digits[j]) + str(digits[i]))
                    if len(str(candidate)) == 3 and candidate %  2 == 0: result.add(candidate)
        return len(result)

# @lc code=end

