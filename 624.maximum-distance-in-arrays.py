#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    For each row, get the max of all row ends except itself and return the minimum abs difference
    '''
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ends = []
        m = len(arrays)
        for i in range(m): heapq.heappush(ends, [- arrays[i][-1], i])
        result = 0
        for i in range(m):
            negEnd, j = heapq.heappop(ends)
            if j == i: 
                negEnd2, j2 = heapq.heappop(ends)
                result = max(result, abs(arrays[i][0] + negEnd2))
                heapq.heappush(ends, [negEnd2, j2])
            else: result = max(result, abs(arrays[i][0] + negEnd))
            heapq.heappush(ends, [negEnd, j])
        return result
            

        
# @lc code=end

