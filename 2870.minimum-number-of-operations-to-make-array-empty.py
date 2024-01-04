#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
from typing import List


class Solution:
    '''
    All counts must be 2 * m + 3 * n
    The best strategy is take:
    1. count // 3 round of 2nd operation, and if (count - 3 * (count // 3)) % 2 == 0, add (count - 3 * (count // 3)) // 2 of 1st operation
    2. Take (count // 3 - 1) round of 2nd operation, and if (count - 3 * (count // 3 - 1)) % 2 == 0, add (count - 3 * (count // 3 - 1)) // 2 of 1st operation
    return -1 otherwise
    '''
    def minOperations(self, nums: List[int]) -> int:
        counts = {}
        for num in nums: counts[num] = counts.get(num, 0) + 1
        result = 0
        for v in counts.values():
            if (v - 3 * (v // 3)) % 2 == 0:
                result += v // 3 + (v - 3 * (v // 3)) // 2
            elif v // 3 > 0 and (v - 3 * ((v // 3) - 1)) % 2 == 0:
                result += v // 3 - 1 + (v - 3 * ((v // 3) - 1)) // 2
            else: return -1
        return result

        
# @lc code=end

