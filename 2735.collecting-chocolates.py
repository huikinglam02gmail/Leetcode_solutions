#
# @lc app=leetcode id=2735 lang=python3
#
# [2735] Collecting Chocolates
#

# @lc code=start
from typing import List


class Solution:
    '''
    let res[k] = cost to collect all chocolates with k rotations. We know that k  < len(nums) as rotating n times is equivalent to no rotations.
    With k rotations, we can choose to get chocolates at index i with min(nums[i - k : i])
    '''
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [k * x for k in range(n)]
        for i in range(n):
            current = float('inf')
            for k in range(n):
                current = min(current, nums[(i - k + n) % n])
                res[k] += current
        return min(res)
# @lc code=end

