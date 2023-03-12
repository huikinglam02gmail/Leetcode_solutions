#
# @lc app=leetcode id=1674 lang=python3
#
# [1674] Minimum Moves to Make Array Complementary
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each pair (a, b), assume a <= b. There are only 3 options: make no move (target = a + b), make 1 move (  a + 1 <= target <= b + limit), or make 2 moves (target <= a or target > b + limit). Simplify the procedure by marking where the transition occurs by prefix sum
    '''
    def minMoves(self, nums: List[int], limit: int) -> int:
        prefix = [0] * 2 * (limit + 1)
        n = len(nums)
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n - 1 - i]])
            prefix[0] += 2
            prefix[a + 1] -= 1
            prefix[a + b] -= 1
            prefix[a + b + 1] += 1
            prefix[b + limit + 1] += 1
        
        result = n
        prefixSum = 0
        for i in range(2*limit + 2):
            prefixSum += prefix[i]
            result = min(result, prefixSum)
        return result
# @lc code=end
