#
# @lc app=leetcode id=3356 lang=python3
#
# [3356] Zero Array Transformation II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Scan through nums. For each num, try using queries from left to right 
    '''
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        S = 0
        k = 0
        n = len(nums)
        counts = [0 for i in range(n + 1)]
        for i in range(n):
            while nums[i] > S + counts[i]:
                if k == len(queries): return -1
                k += 1
                l, r, val = queries[k - 1]
                if r >= i: 
                    counts[max(l, i)] += val
                    counts[r + 1] -= val
            S += counts[i]
        return k
# @lc code=end

