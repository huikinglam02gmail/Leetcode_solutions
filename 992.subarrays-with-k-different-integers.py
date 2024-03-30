#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from typing import List


class Solution:
    '''
    A sliding window problem
    It is rather hard to count subarrays with exactly k different integers
    But we can tweak the question a little bit:
    number of good subarrays = number of subarray with at most k different integers - number of subarrays with at most k - 1 different integers 
    '''
    def subarraysWithLessThanOrEqualToKDistinct(self, nums, k):
        counter = {}
        l = 0
        res = 0
        for r in range(len(nums)):
            counter[nums[r]] = counter.get(nums[r], 0) + 1
            while len(counter) > k:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0: counter.pop(nums[l])
                l += 1
            res += r - l + 1
        return res
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithLessThanOrEqualToKDistinct(nums, k) - self.subarraysWithLessThanOrEqualToKDistinct(nums, k - 1)
# @lc code=end

