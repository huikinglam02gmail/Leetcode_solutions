#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False for i in range(len(nums))]
        heap = []
        for i, num in enumerate(nums): heapq.heappush(heap, [num, i])
        result = 0
        while heap:
            while heap and marked[heap[0][1]]: heapq.heappop(heap)
            if heap:
                num, i = heapq.heappop(heap)
                result += num
                marked[i] = True
                if i > 0: marked[i - 1] = True
                if i < len(nums) - 1: marked[i + 1] = True
        return result
# @lc code=end

