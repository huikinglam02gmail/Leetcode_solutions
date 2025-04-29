#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum =  max(nums)
        hashTable = {}
        l = 0
        result = 0
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
            while hashTable.get(maxNum, 0) >= k:
                hashTable[nums[l]] -= 1
                l += 1
            result += l
        return result
# @lc code=end

