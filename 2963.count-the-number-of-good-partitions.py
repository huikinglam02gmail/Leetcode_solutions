#
# @lc app=leetcode id=2963 lang=python3
#
# [2963] Count the Number of Good Partitions
#

# @lc code=start
from typing import List


class Solution:
    '''
    requirement is all occurrence of a nums[i] must be in a single subarray.
    let right[nums[i]] = rightmost appearance index of nums[i]
    when scan from left to right, keep track of the last rightmost good partition subarray index.
    if it is smaller than current index, we can multiply the result by 2
    E.g. in [1, 2, 3, 4], 1 can be alone or join with the following indices. So possibilities *= 2 each time 
    '''
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        right = {}
        for i in range(len(nums)): right[nums[i]] = i
        result = 1
        maxRight = 0
        MOD = 1000000007
        for i in range(len(nums)):
            if maxRight < i:
                result *= 2
                result %= MOD
            maxRight = max(maxRight, right[nums[i]])        
        return result
# @lc code=end

