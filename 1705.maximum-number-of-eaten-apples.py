#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Eat the fast rotting apples first
    '''
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        n = len(apples)
        result = 0
        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(heap, [i + days[i], apples[i]])
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                deadline, apple = heapq.heappop(heap)
                result += 1
                if apple > 1:
                    heapq.heappush(heap, [deadline, apple - 1])
        date = n
        while heap:
            while heap and heap[0][0] <= date:
                heapq.heappop(heap)
            if heap:
                deadline, apple = heapq.heappop(heap)
                canEat = min(deadline - date, apple)
                result += canEat
                date += canEat
        return result
        
# @lc code=end

