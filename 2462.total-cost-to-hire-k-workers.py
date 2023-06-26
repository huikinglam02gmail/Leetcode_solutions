#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap, right_heap, used = [], [], set()
        n = len(costs)
        left, right = -1, n
        
        result, count = 0, 0
        for i in range(candidates):
            heapq.heappush(left_heap, [costs[i], i])
            left += 1
        for i in range(n-1, n-1-candidates,-1):
            heapq.heappush(right_heap, [costs[i], i])
            right -= 1            
        while left < n and right >= 0 and count < k:
            left_min_cost, left_min_ind = heapq.heappop(left_heap)
            right_min_cost, right_min_ind = heapq.heappop(right_heap)
            if left_min_cost <= right_min_cost:
                result += left_min_cost
                heapq.heappush(right_heap,[right_min_cost, right_min_ind])
                left += 1
                while left in used:
                    left += 1
                if left < n:
                    heapq.heappush(left_heap, [costs[left], left])
                used.add(left_min_ind)
            else:
                result += right_min_cost
                heapq.heappush(left_heap,[left_min_cost, left_min_ind])
                right -= 1
                while right in used:
                    right -= 1
                if right >= 0:
                    heapq.heappush(right_heap, [costs[right], right])
                used.add(right_min_ind)
            while left_heap and left_heap[0][1] in used:
                heapq.heappop(left_heap)
            while right_heap and right_heap[0][1] in used:
                heapq.heappop(right_heap)             
            count += 1
        if count < k:
            heap = []
            for i in range(n):
                if i not in used:
                    heapq.heappush(heap, [costs[i],i])
            for i in range(count, k):
                result += heapq.heappop(heap)[0]
        return result
        
# @lc code=end

