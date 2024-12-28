#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    Very similar to trapping rain water
    First: convert to subarray sum
    The mission is to pick three out of the subarray sum, provided that the ranges the sum picks cannot overlap
    For example, if i, j, l are picked as starting point of the interval (the answer)
    i <= j - k and l >= j + k must be obeyed. We aim to maximize arr_sum(i) + arr_sum(j) + arr_sum(k)
    if we pick j to be scanned through the array, Notice this is very similar to the trapping rain water problem
    Notice to get the lexicographically smallest, we do not allow equal when calculating left and do when calculating right    
    '''
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        array_sum = []
        for i in range(len(nums) - k + 1):
            if i == 0: array_sum.append(sum(nums[:k]))
            else: array_sum.append(array_sum[-1] - nums[i - 1] + nums[i - 1 + k])
        left = [0]
        largest = 0
        for i in range(1, len(array_sum)):
            if array_sum[i] > array_sum[largest]: largest = i
            left.append(largest)
        right = [len(array_sum) - 1 for i in range(len(array_sum))]
        largest = len(array_sum) - 1
        for i in range(len(array_sum)-2, -1,-1):
            if array_sum[i] >= array_sum[largest]: largest = i
            right[i] = largest
        max_so_far = 0
        for j in range(k, len(array_sum) - k):
            i, l = left[j - k], right[j + k]
            if array_sum[i] + array_sum[j] + array_sum[l] > max_so_far:
                max_so_far = array_sum[i] + array_sum[j] + array_sum[l]
                result = [i, j, l]
        return result
        
# @lc code=end

