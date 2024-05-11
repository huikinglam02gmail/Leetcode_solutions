#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    A optimization problem depending on greedy choice of cheap labour and kicking out high quality expensive workers
    In this problem, there is a varying "worthiness" of different workers, signified by wage[i] / quality[i]. The lower the value, the cheaper the worker
    But given k can vary between the whole array length and very short, It is possible that when k is relatively large, expensive workers can put drastically raise the the pay for cheaper workers with high quality.
    Therefore we would like to use a max heap which stores the quality of considered workers. When length of heap is larger than k, we pop out the workers of largest quality    
    '''
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([[wage[i] / quality[i], quality[i]] for i in range(len(quality))])
        heap = []
        q_sum, result = 0, float('inf')
        for r, q in ratio:
            q_sum += q
            heapq.heappush(heap, -q)
            if len(heap) > k: q_sum += heapq.heappop(heap)
            if len(heap) == k: result = min(result, q_sum * r)
        return result
# @lc code=end

