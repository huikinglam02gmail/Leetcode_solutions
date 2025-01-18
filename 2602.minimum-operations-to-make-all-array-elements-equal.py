#
# @lc app=leetcode id=2602 lang=python3
#
# [2602] Minimum Operations to Make All Array Elements Equal
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    sort nums and queries.
    prepare prefix sum of nums
    for each query, the ans is 
    '''
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for num in nums: prefix.append(prefix[-1] + num)
        queryDict = {}
        queryInd = {}
        for i, q in enumerate(queries):
            if q not in queryInd: queryInd[q] = []
            queryInd[q].append(i)
        queries.sort()
        for q in queries:
            if q not in queryDict:
                queryDict[q] = 0
                countSmaller = bisect.bisect_left(nums, q)
                queryDict[q] += q * countSmaller - prefix[countSmaller]
                countLarger = len(nums) - bisect.bisect_right(nums, q)
                queryDict[q] += prefix[-1] - prefix[len(nums) - countLarger] - q * countLarger
        result = [0] * len(queries)
        for key in queryDict:
            for i in queryInd[key]:
                result[i] = queryDict[key]
        return result
# @lc code=end

