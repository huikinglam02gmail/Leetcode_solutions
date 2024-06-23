#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    # We can use a sliding window technique to handle the problem
    # First set left = 0, and loop through nums with right
    # We first check right against the max and min heap top
    # if the absolute difference is larger than limit, we pop it and update left to be max of popped index + 1 and left
    # After that we make sure the heap top has index >= left
    # Keep doing so until the conditions are satisfied
    # update result to be max(result, right - left + 1)    
    
    '''

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result, left = 0, 0
        max_heap, min_heap = [], []
        for right, num in enumerate(nums):
            while max_heap and abs(-max_heap[0][0] - num) > limit:
                item, index = heapq.heappop(max_heap)
                left = max(left, index + 1)
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)
            heapq.heappush(max_heap,[-num, right])
            while min_heap and abs(min_heap[0][0] - num) > limit:
                item, index = heapq.heappop(min_heap)
                left = max(left, index + 1)
                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)
            heapq.heappush(min_heap,[num, right])
            result = max(result, right - left + 1)
        return result
# @lc code=end

