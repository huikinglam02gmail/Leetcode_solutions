#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
from typing import List


class Solution:
    '''
    Linear search is trivial. To do it in log(n) time, we should note that for no missing positive integers, arr[i] = i + 1. Any discrepancy is given by arr[i] - i - 1 = number of positive integers missing for arr[:i+1]. This array must be strictly nondecreasing. Then we are looking for the first leftmost index ans(bisectleft) in which arr[i] - i - 1 <= k. Then return ans + k
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return left + k

# @lc code=end

