#
# @lc app=leetcode id=2025 lang=python3
#
# [2025] Maximum Number of Ways to Partition an Array
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    The best way to understand what's happening is to put an example array in Excel and observe what happens
    Prepare the prefix sum and suffix sum arrays.
    If we leave the array unchanged, the number of pivots is number of indices in which prefix[i] == suffix[i + 1], i in [0, n - 2]
    We first count this number
    If we change nums[i] to k,  prefix[j] += (k - nums[i]), j = i,...,n - 1; suffix[j] += k - nums[i], j = 0, ... , i
    Then for each nums[i], we consider if nums[j] is changed to k:
    1. if i < j: prefixNew[i] = prefix[i] and suffixNew[i + 1] = suffix[i + 1] + k - nums[j]
    2. if j <= i: prefixNew[i] = prefix[i] + k - nums[j] and suffixNew[i + 1] = suffix[i + 1]
    i.e. a pivot exist between nums[i] and nums[i + 1] if nums[j] is change to k, in either one of these 2 cases:
    1. for j > i, nums[j] - k = - (prefix[i] - suffix[i + 1])
    2. for j <= i, nums[j] - k =  (prefix[i] - suffix[i + 1])
    To find the number of possible pivots if we change nums[i] to k, we look at j < i for k - nums[i] and j >= i for nums[i] - k, in the hash map of prefix[i] - suffix[i + 1]
    '''
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n, result = len(nums), 0
        prefixSum, suffixSum = [num for num in nums], [num for num in nums]
        left, right = {}, {}
        for i in range(1, n): prefixSum[i] += prefixSum[i - 1]
        for i in range(n - 2, -1, -1): 
            suffixSum[i] += suffixSum[i + 1]
            if suffixSum[i + 1] == prefixSum[i]: result += 1
            diff = prefixSum[i] - suffixSum[i + 1]
            if diff not in right: right[diff] = deque()
            right[diff].append(i)
        for i in range(n):
            current = len(left.get(k - nums[i], deque())) + len(right.get(nums[i] - k, deque()))
            result = max(result, current)
            if i < n - 1:
                diff = prefixSum[i] - suffixSum[i + 1]
                right[diff].popleft()
                if diff not in left: left[diff] = deque()
                left[diff].append(i)
        return result
        
# @lc code=end

