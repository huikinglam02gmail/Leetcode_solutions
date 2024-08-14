#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
from typing import List


class Solution:
    '''
    As suggested by the hint, use binary search
    Firstly, to do binary search we need to first sort the distance array (nC2 in length)
    But we actually do not need to calculate it as long as we can sort the original array
    Instead, we use two-pointer algorithm to count how many pairs has difference smaller than d
    for example, if nums[j] - nums[i] > d, j += 1, count += j - i
    if count is larger or equal to k, we might have reached a solution. record the answer and try exploring with the right becomes mid - 1
    else: we guess is too small and we increase the left estimate to be mid + 1    
    '''
    def pair_distance(self, distance, k):
        i, count = 0, 0
        for j, x in enumerate(self.arr):
            while x - self.arr[i] > distance: i += 1
            count += j - i
        return count >= k
        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        self.arr = sorted(nums)
        left, right = 0, self.arr[-1] - self.arr[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.pair_distance(mid, k): right = mid
            else: left = mid + 1
        return left
# @lc code=end

