#
# @lc app=leetcode id=1906 lang=python3
#
# [1906] Minimum Absolute Difference Queries
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    1 <= nums[i] <= 100
    We can save indices of appearance of each nums
    Then binary search for each query
    '''
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        hashTable = {}
        for i, num in enumerate(nums):
            hashTable[num] = hashTable.get(num, []) + [i]
        
        allNums = sorted(hashTable.keys())
        result = []
        for l, r in queries:
            appeared = []
            result.append(float("inf"))
            for allNum in allNums:
                if bisect.bisect_right(hashTable[allNum], r) - bisect.bisect_left(hashTable[allNum], l) > 0:
                    appeared.append(allNum)
                    if len(appeared) > 1:
                        result[-1] = min(result[-1], appeared[-1] - appeared[-2])
            if result[-1] == float("inf"):
                result[-1] = - 1
        return result

        
# @lc code=end

