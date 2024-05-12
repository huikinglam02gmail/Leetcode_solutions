#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import bisect
from typing import List



class Solution:
    '''
    Binary search-based solution
    Since the matrix is sorted in both directions, we can binary search on the number of elements less than or equal to mid
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for row in matrix: count += bisect.bisect_right(row, mid)
            if count >= k: right = mid
            else: left = mid + 1
        return left
# @lc code=end

