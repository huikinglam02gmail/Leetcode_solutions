#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List
import bisect


class Solution:
    '''
    We should note that to get to maximum possible frequency, the number must be one of nums. One must be incrementing numbers smaller than it. 
    Therefore, we should sort nums
    For example if we have nums sorted as [a, b, c, d], which a <= b <= c <= d, the cost to get all of them into d in d - a + d - b + d - c = 3 * d - (a + b + c)
    = (i - j) * nums[i] - (prefixSum[i] - prefixSum[j]).
    In here i = 3 and j = 0. Next, we can use sliding window explore all the possible windows
    '''
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        result = 0
        j = 0
        n = len(nums)
        for i in range(n):
            while (i - j) * nums[i] - prefix[i] + prefix[j] > k:
                j += 1
            result = max(result, i + 1 - j)
        return result
        
# @lc code=end

