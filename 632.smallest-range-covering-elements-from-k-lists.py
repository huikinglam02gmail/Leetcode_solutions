#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''        
    The idea is to go through one of the lists from min to max
    at the beginning, push the first element of each list with its row and column indices into a min heap. Then at each round, find min element from the heap. Get the next larger number in that row. We keep track of the largest element inside the heap. Because in each pop, we always remove one element and add back another element to the heap, the heap always keeps one element of each list inside the heap. The difference between the largest element in the heap (maxsofar) and the smallest element (the front of the heap) is kept tracked of. The process ends when one of the lists arrived at the end (further element addition from a different row will violate the one row - one element condition). 
    '''
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        globalMax, globalMin, maxSoFar = - float('inf'), float('inf'), - float('inf')
        heap = []
        for i, num in enumerate(nums):
            globalMax = max(globalMax, num[-1])
            globalMin = min(globalMin, num[0])
            heapq.heappush(heap, [num[0], i, 0])
            maxSoFar = max(maxSoFar,num[0])
            
        result = [globalMin, globalMax]
        diff = globalMax - globalMin
        
        while heap:
            num, row, col = heapq.heappop(heap)
            if maxSoFar - num < diff:
                diff = maxSoFar - num
                result = [num, maxSoFar]
            if col < len(nums[row]) - 1:
                heapq.heappush(heap, [nums[row][col + 1], row, col + 1])
                maxSoFar = max(maxSoFar, nums[row][col + 1])
            else:
                break
        return result
# @lc code=end